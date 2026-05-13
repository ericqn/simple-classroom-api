from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

GRADE_ORDER = ["freshman", "sophomore", "junior", "senior"]
classnames = {
    "CSCI 100": {
        "description": "Freshman level computer science course", 
        "min_grade": "freshman",
        "prerequisite": []
    },
    "CSCI 200": {
        "description": "Sophomore level computer science course", 
        "min_grade": "sophomore",
        "prerequisite": []
    },
    "CSCI 300": {
        "description": "Junior level computer science course", 
        "min_grade": "junior",
        "prerequisite": ["CSCI 100", "CSCI 200"]
    },
    "CSCI 400": {
        "description": "Senior level computer science course", 
        "min_grade": "senior",
        "prerequisite": ["CSCI 300"]
    },
    "CSCI 500": {
        "description": "Master's level computer science course", 
        "min_grade": "senior",
        "prerequisite": ["CSCI 400"]
    },
    "CSCI 600": {
        "description": "PhD level computer science course", 
        "min_grade": "senior",
        "prerequisite": ["CSCI 500"]
    },
}


@app.get("/")
def root():
    return "Welcome to class"

@app.post("/classnames")
def create_classnames(name: str, min_grade: str, desc: str, prereq: list[str] = Query(default=[])):
    classnames[name] = {"description": desc,
                             "min_grade": min_grade,
                             "prerequisite": prereq}
    return classnames[name]

@app.get("/classnames")
def all_classnames():
    return classnames

@app.get("/classnames/filter")
def filtered_classnames(min_grade: str):
    min_index = GRADE_ORDER.index(min_grade)
    return {k:v for k, v in classnames.items() if GRADE_ORDER.index(v["min_grade"]) >= min_index}

@app.get("/classnames/{name}")
def indiv_classnames(name: str):
    if name not in classnames:
        raise HTTPException(status_code=404, detail="Class not found")
    return classnames[name]

@app.delete("/classnames/{name}")
def delete_classname(name: str):
    if name not in classnames:
        raise HTTPException(status_code=404, detail="Class not found")
    del classnames[name]
    return {"deleted": name}

@app.patch("/classnames/{name}")
def change_classname(name: str, desc: str = None, min_grade: str = None, prereq: list[str] = Query(default=None), clear_prereq: bool = False):
    if name not in classnames:
        raise HTTPException(status_code=404, detail="Class not found")
    if desc is not None:
        classnames[name]["description"] = desc
    if min_grade is not None:
        classnames[name]["min_grade"] = min_grade
    if clear_prereq:
        classnames[name]["prerequisite"] = []
    elif prereq is not None:
        classnames[name]["prerequisite"] = prereq
    return classnames[name]