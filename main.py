from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Class, User
import random

app = FastAPI()
Base.metadata.create_all(bind=engine)

# prevents connection leaks that would occur if a single global session were shared
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return "Welcome to class"

# ===================== Classes =====================

@app.post("/classnames")
def create_classnames(user_id: int,
                      name: str, 
                      max_enrollment: int,
                      min_grade: int, 
                      desc: str, 
                      prereq: list[str] = Query(default=[]), 
                      alias: list[str] = Query(default=[]),
                      subject_tags: list[str] = Query(default=[]),
                      db: Session = Depends(get_db)):

    # verify creator exists
    creator = db.query(User).filter(User.id == user_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="User not found")
    # create new class
    new_class = Class(class_name=name,
                      description=desc,
                      min_grade=min_grade,
                      prerequisites=prereq,
                      students_enrolled=[],
                      max_enrollment=max_enrollment,
                      alias=alias,
                      subject_tags=subject_tags,
                      owner_id=user_id)
    db.add(new_class)
    # update creator's published classes
    creator.published_classes = creator.published_classes + [name]
    db.commit()
    db.refresh(new_class)
    return new_class

@app.get("/classnames")
def all_classnames(user_id: int, db: Session = Depends(get_db)):
    return db.query(Class).all()

@app.get("/classnames/filter")
def filtered_classnames(user_id: int, min_grade: int, db: Session = Depends(get_db)):
    return db.query(Class).filter(Class.min_grade >= min_grade).all()

@app.get("/classnames/{name}")
def indiv_classnames(user_id: int, name: str, db: Session = Depends(get_db)):
    obj = db.query(Class).filter(Class.class_name == name).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return obj

@app.delete("/classnames/{name}")
def delete_classname(name: str, user_id: int, db: Session = Depends(get_db)):
    # verify requester has permission
    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.admin_level == "student":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    # delete class from db
    obj = db.query(Class).filter(Class.class_name == name).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(obj)
    db.commit()
    return {"deleted": name}

@app.patch("/classnames/{name}")
def change_classname(user_id: int,
                     name: str, 
                     desc: str = None, 
                     min_grade: int = None, 
                     prereq: list[str] = Query(default=None), 
                     clear_prereq: bool = False, 
                     db: Session = Depends(get_db)):
    # fetch class
    obj = db.query(Class).filter(Class.class_name == name).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Class not found")
    # updates
    if desc is not None:
        obj.description = desc
    if min_grade is not None:
        obj.min_grade = min_grade
    if clear_prereq:
        obj.prerequisites = []
    elif prereq is not None:
        obj.prerequisites = prereq
    db.commit()
    db.refresh(obj)
    return obj

# ===================== Users =====================

@app.get("/users")
def all_users(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/filter")
def filter_users(user_id: int, grade: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.grade_level == grade).all()

@app.get("/users/enrolled")
def users_by_class(user_id: int, class_name: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.enrolled_classes.contains([class_name])).all()

@app.post("/users")
def create_user(name: str,
                grade_level: int,
                admin_level: str,
                db: Session = Depends(get_db)):
    
    new_user = User(name=name, 
                    grade_level=grade_level, 
                    admin_level=admin_level, 
                    enrolled_classes=[], 
                    published_classes=[])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/users/{user_id}/level")
def change_user_level(user_id: int, new_level: str, requester_id: int, db: Session = Depends(get_db)):
    # verify requester is an admin
    requester = db.query(User).filter(User.id == requester_id).first()
    if not requester or requester.admin_level != "admin":
        raise HTTPException(status_code=403, detail="Only admins can change user levels")
    # verify target exists and is not an admin
    target = db.query(User).filter(User.id == user_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="User not found")
    if target.admin_level == "admin":
        raise HTTPException(status_code=403, detail="Cannot change another admin's level")
    # update level
    target.admin_level = new_level
    db.commit()
    db.refresh(target)
    return target

@app.patch("/users/{user_id}/taken")
def update_taken_classes(user_id: int, class_name: str, db: Session = Depends(get_db)):
    # get user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # append completed class
    user.enrolled_classes = user.enrolled_classes + [class_name]
    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}/classes/{class_name}")
def unenroll(user_id: int, class_name: str, db: Session = Depends(get_db)):
    # get user and class
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    obj = db.query(Class).filter(Class.class_name == class_name).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Class not found")
    # remove class from user and user from class
    user.enrolled_classes = [c for c in user.enrolled_classes if c != class_name]
    obj.students_enrolled = [sid for sid in obj.students_enrolled if sid != user_id]
    db.commit()
    return {"unenrolled": class_name}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, requester_id: int, db: Session = Depends(get_db)):
    # verify requester has sufficient permissions
    requester = db.query(User).filter(User.id == requester_id).first()
    if not requester or requester.admin_level == "student":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    # delete user from db
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"deleted": user_id}

@app.post("/users/{user_id}/enroll")
def enroll(user_id: int, class_name: str, db: Session = Depends(get_db)):
    # get user and class
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    obj = db.query(Class).filter(Class.class_name == class_name).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Class not found")
    # check capacity
    if len(obj.students_enrolled) >= obj.max_enrollment:
        raise HTTPException(status_code=400, detail="Class is full")
    # enroll user in class
    obj.students_enrolled = obj.students_enrolled + [user_id]
    user.enrolled_classes = user.enrolled_classes + [class_name]
    db.commit()

    # Paul easter egg
    if random.random() < 0.01:
        paul = db.query(User).filter(User.name == "Paul Elliott").first()
        if paul:
            # add Paul and ping pong prerequisite
            obj.students_enrolled = obj.students_enrolled + [paul.id]
            if "Ping Pong" not in obj.prerequisites:
                obj.prerequisites = obj.prerequisites + ["Ping Pong"]
            # remove students that don't have ping pong completed
            remaining = []
            for sid in obj.students_enrolled:
                student = db.query(User).filter(User.id == sid).first()
                if student and "Ping Pong" in (student.enrolled_classes or []):
                    remaining.append(sid)
            obj.students_enrolled = remaining
        db.commit()

    db.refresh(obj)
    return obj
