# Overview: 
Create an API that manages signing up for student classes. Curate a base set of classes that your API provides (at least 6) and enable the user to see the information of these classes and sign up for ones that they like. Allow for an instructor on the platform to create their own classes.

## Objective: 

Learn the basics on some of the backend APIs we will be using. You will be spending roughly a week to do the following:

## Important Notes: 

PLEASE DO NOT COMMIT TO MAIN. Each one of these parts should be you creating ONE new branch + pull request (PR) in your repository. Ideally, each of your commits should also encompass one of the bullet points specified for each part. After each one of these parts, please create an PR and assign me as the reviewer. I will read over your code and provide comments if necessary. 

The exact details of this project are largely omitted, so you will be tasked with designing some of the more granular features like the function headers, parameters, file structure, etc. In the review, I will mainly be looking to see if you have followed the part instructions, completed the deliverables (if provided), and maintained clean code formatting and structure.

## Part 1: FastAPI Basics (1-2 days)

Deliverables:

- Learn the basics of REST architecture (GET, POST, PATCH, DELETE, etc.). Learn why each method is important, where they can be used, and the benefits of using REST architecture.
- Setup FastAPI + uvicorn in your project folder/repo. Create at least one endpoint for each of the following methods above. Try to match these to eventually fit the classroom-like API mentioned in the overview. You may need more than just 4 endpoints.
- For your initial data storage, you can use some simple data structure (like an array or map) to store simple data like strings. This should be enough to persist throughout the time where your API server is up.
- Host your new API locally using uvicorn library
- FastAPI comes with a built-in documentation handler and tester, hosted on Swagger UI. Create requests to each of your endpoints using the Swagger UI to see what happens.
- Learn to use cURL to hit each of your endpoints from the computer terminal.
- Example command: 
```bash
curl -X GET "http://localhost:8000/api/my-test-endpoint"
```
By the end of this stage, ensure that your endpoints can do the following:
- A user can view the catalog of class names
- A user can view the catalog of class names filtered by minimum grade level.
- A user can view the description, minimum grade level, and prerequisites when giving information of the class name.
- A user can create a new class by specifying details like description, minimum grade level, and prerequisites.
- A user can delete a class by specifying the class name and/or id.
- A user can update an existing class description and minimum grade level.

## Part 2: FastAPI + pydantic (1 day)

Deliverables:

- Import pydantic into your project repo
- Formalize your school class object by creating a pydantic schema that inherits from the pydantic BaseModel class.
- pydantic allows you to ensure data sent into your API fits a certain standard and/or format. if a bad actor is to use your API, they are prevented from sending in bad requests
- Upgrade your API to take in specific simple schemas you've built from pydantic (at least 3 fields)

## Part 3: sqlalchemy/PostgreSQL basics (2-3 days)

- Import sqlalchemy
- Setup a database using postgreSQL + sqlalchemy.
- Store your school class objects that you created in parts ½
- Create a schema to store a user that can be either a student or an instructor type. Include basic information like name, classes taken, classes taught, etc. If you haven't already, create a POST endpoint that allows a user to add a class into the database ONLY if they are of "instructor" status.
- Update your endpoints in parts 1 and 2 to actually do inserts into the database tables you created
- Update your endpoints in parts 1 and 2 to require passing through user ids.

## Part 4: Meet all deliverables criteria

- Allow a user to view the description and prerequisites of a specific class after sending a request containing the class name and user ID. If the user is an instructor, allow the user to see what students have signed up for the class they have posted.
- If the user is an instructor, allow this user to create a class that provides information of: class name, class name aliases, subject tags, prerequisites, students enrolled, max enrollment number, minimum grade level

- Eric TODO : Add more deliverables