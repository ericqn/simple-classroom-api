GRADE_ORDER = ["freshman", "sophomore", "junior", "senior"]
classnames = {
    "CSCI 100": {
        "description": "Freshman level computer science course", 
        "min_grade": 1,
        "prerequisite": []
    },
    "CSCI 200": {
        "description": "Sophomore level computer science course", 
        "min_grade": 2,
        "prerequisite": []
    },
    "CSCI 300": {
        "description": "Junior level computer science course", 
        "min_grade": 3,
        "prerequisite": ["CSCI 100", "CSCI 200"]
    },
    "CSCI 400": {
        "description": "Senior level computer science course", 
        "min_grade": 4,
        "prerequisite": ["CSCI 300"]
    },
    "CSCI 500": {
        "description": "Master's level computer science course", 
        "min_grade": 4,
        "prerequisite": ["CSCI 400"]
    },
    "CSCI 600": {
        "description": "PhD level computer science course", 
        "min_grade": 4,
        "prerequisite": ["CSCI 500"]
    },
}