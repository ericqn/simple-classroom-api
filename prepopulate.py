from database import SessionLocal
from models import Class, User

db = SessionLocal()

starter_classes = [
    Class(class_name="CSCI 100", description="Freshman level CS course", min_grade=1, prerequisites=[], students_enrolled=[], max_enrollment=30, alias=["EE 100"], subject_tags=["cs"]),
    Class(class_name="CSCI 200", description="Sophomore level CS course", min_grade=2, prerequisites=[], students_enrolled=[], max_enrollment=30, alias=["EE 200"], subject_tags=["cs"]),
    Class(class_name="CSCI 300", description="Junior level CS course", min_grade=3, prerequisites=["CSCI 100"], students_enrolled=[], max_enrollment=30, alias=["EE 300"], subject_tags=["cs"]),
    Class(class_name="CSCI 400", description="Senior level CS course", min_grade=4, prerequisites=["CSCI 300"], students_enrolled=[], max_enrollment=30, alias=["EE 400"], subject_tags=["cs"]),
    Class(class_name="CSCI 500", description="Master's level CS course", min_grade=4, prerequisites=["CSCI 400"], students_enrolled=[], max_enrollment=20, alias=["EE 500"], subject_tags=["cs"]),
    Class(class_name="CSCI 600", description="PhD level CS course", min_grade=4, prerequisites=["CSCI 500"], students_enrolled=[], max_enrollment=10, alias=["EE 600"], subject_tags=["cs"])
]

paul = User(name = "Paul Elliott", grade_level=67, admin_level="student")
administrator = User(name="Dean", admin_level="admin")

if not db.query(Class).first():
    db.add_all(starter_classes)
    db.add(paul)
    db.add(administrator)
    db.commit()
    print("Database prepopulated")
else:
    print("Database already populated, skipping")
db.close()
