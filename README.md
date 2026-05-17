**Endpoints created for:**

*Classes*
1) Full class visualization
2) Filter classes by minimum grade level
3) Individual class details
4) Create a new class (sets owner, updates published classes)
5) Update specific class description, grade, or prerequisites
6) Delete a class (instructor or above only)
7) Enroll a user in a class (with max enrollment check + Paul Elliott easter egg)

*Users*
1) Full user visualization
2) Filter users by grade level
3) Find users enrolled in the same class
4) Create a new user
5) Change a user's admin level (admin only, cannot target other admins)
6) Update classes a user has taken
7) Unenroll a user from a class
8) Delete a user (instructor or above only)

**Database setup**
PostgreSQL + SQLAlchemy. Two tables: `classes` and `users`.

Start PostgreSQL:
`brew services start postgresql@15`

Start server (creates tables on startup):
`uvicorn main:app --reload`

Seed the database (run once):
`python prepopulate.py`

**Swagger UI testing**
`http://localhost:8000/docs`

**cURL testing:**

Getting all classes
`curl -X GET "http://localhost:8000/classnames?user_id=1"`

Getting a specific class
`curl -X GET "http://localhost:8000/classnames/CSCI%20300?user_id=1"`

Filtering classes by minimum grade level
`curl -X GET "http://localhost:8000/classnames/filter?user_id=1&min_grade=3"`

Adding a class
`curl -X POST "http://localhost:8000/classnames?user_id=1&name=CSCI%20700&min_grade=4&desc=Advanced+topics&max_enrollment=20"`

Updating a class
`curl -X PATCH "http://localhost:8000/classnames/CSCI%20100?user_id=1&desc=Updated+description"`

Deleting a class (instructor or above)
`curl -X DELETE "http://localhost:8000/classnames/CSCI%20100?user_id=1"`

Enrolling a user in a class
`curl -X POST "http://localhost:8000/users/1/enroll?class_name=CSCI%20100"`

Getting all users
`curl -X GET "http://localhost:8000/users?user_id=1"`

Filtering users by grade level
`curl -X GET "http://localhost:8000/users/filter?user_id=1&grade=2"`

Finding users enrolled in a class
`curl -X GET "http://localhost:8000/users/enrolled?user_id=1&class_name=CSCI%20100"`

Creating a user
`curl -X POST "http://localhost:8000/users?name=Ethan&grade_level=2&admin_level=student"`

Changing a user's admin level (admin only)
`curl -X POST "http://localhost:8000/users/2/level?requester_id=1&new_level=instructor"`

Updating a user's taken classes
`curl -X PATCH "http://localhost:8000/users/1/taken?class_name=CSCI%20100"`

Unenrolling a user from a class
`curl -X DELETE "http://localhost:8000/users/1/classes/CSCI%20100"`

Deleting a user (instructor or above)
`curl -X DELETE "http://localhost:8000/users/2?requester_id=1"`
