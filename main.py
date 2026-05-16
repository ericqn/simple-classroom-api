from fastapi import FastAPI, HTTPException, Query
from data import classnames

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to class"

@app.post("/classnames")
def create_classnames(name: str, 
                      min_grade: int, 
                      desc: str, 
                      prereq: list[str] = Query(default=[])):
    classnames[name] = {"description": desc,
                             "min_grade": min_grade,
                             "prerequisite": prereq}
    return classnames[name]

@app.get("/classnames")
def all_classnames():
    return classnames

@app.get("/classnames/filter")
def filtered_classnames(min_grade: str):
    return {k:v for k, v in classnames.items() if v["min_grade"] >= min_grade}

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
def patch_class_details(name: str, 
                     desc: str = None, 
                     min_grade: int = None, 
                     prereq: list[str] = Query(default=None), 
                     clear_prereq: bool = False):
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