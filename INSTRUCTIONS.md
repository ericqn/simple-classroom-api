## Objective: Learn the basics on some of the backend APIs we will be using. Spend 4-6 days to do the following:
Create an API that manages signing up for student classes. Curate a set of classes that your API provides (at least 6) and enable the user to see the descriptions of these classes and sign up for ones that they like. Allow for instructor users to 

Important Notes: 

Each one of these parts should be ONE pull request in your repository. After each one of these parts, please create an MR and assign me as the reviewer. I will read over your code and provide comments if necessary.

Part 1: FastAPI Basics (1-2 days)

Deliverables:

- Learn the basics of REST architecture (GET, POST, PATCH, DELETE, etc.). Why is each method important, where they can be used, and the benefits of using REST architecture.
- Setup FastAPI + uvicorn in your project folder/repo. Create at least one endpoint for each of the following methods above
- For simple data storage, you can use some simple data structure (like an array or map) to store simple data like strings
- Host your new API locally using uvicorn library
- FastAPI comes with a built-in documentation handler and tester, hosted on Swagger UI. Create requests to each of your endpoints using the Swagger UI to see what happens.
- Learn to use cURL to hit each of your endpoints from the computer terminal.
- Example command: curl -X GET "http://localhost:8000/api/my-test-endpoint"

Part 2: FastAPI + pydantic (1 day)

Deliverables:

- Import pydantic into your project repo
- Formalize your school class object by creating a pydantic schema that inherits from the pydantic BaseModel class.
- pydantic allows you to ensure data sent into your API fits a certain standard and/or format. if a bad actor is to use your API, they are prevented from sending in bad requests
- Upgrade your API to take in specific simple schemas you've built from pydantic (at least 3 fields)

Part 3: sqlalchemy/PostgreSQL basics (2-3 days)

- Import sqlalchemy
- Setup a database using postgreSQL + sqlalchemy.
- Store your school class objects that you created in parts ½
- Create a schema to store a user that can be either a student or an instructor type. Include basic information like name, classes taken, classes taught, etc. If you haven't already, create a POST endpoint that allows a user to add a class into the database ONLY if they are of "instructor" status.
- Update your endpoints in parts 1 and 2 to actually do inserts into the database tables you created
- Update your endpoints in parts 1 and 2 to require passing through user ids.

Part 4: Meet all deliverables criteria

- Eric TODO