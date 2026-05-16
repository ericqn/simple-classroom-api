**Endpoints created for:**
1) Full classname visualization
2) Filter by minimum grade
    - sorted by [freshman, sophomore, junior, senior]
3) Individual classname
4) Delete specific classname
5) Update specific classname

**uvicorn hosting**
`uvicorn main:app --reload`

*Testing*
`http://localhost:8000/docs`

**cURL testing:**
Getting all classes
`curl -X GET "http://localhost:8000/classnames"`

Getting a specific class
`curl -X GET "http://localhost:8000/classnames/CSCI%20300"`

Filtering by grade level
`curl -X GET "http://localhost:8000/classnames/filter?min_grade=junior"`

Adding a class
`curl -X POST "http://localhost:8000/classnames?name=CSCI%20700&min_grade=senior&desc=Advanced+topics&prereq=CSCI%20500&prereq=CSCI%20600"`

Updating an existing class
`curl -X PATCH "http://localhost:8000/classnames/CSCI%20100?desc=Updated+description"`

Deleting a specific class
`curl -X DELETE "http://localhost:8000/classnames/CSCI%20100"`

