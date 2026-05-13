# Overview: 
Create an API that manages signing up for student classes. Curate a base set of classes that your API provides (at least 6) and enable the user to see the information of these classes and sign up for ones that they like. Allow for an instructor on the platform to create their own classes.

## Objective: 

Learn the basics on some of the backend APIs we will be using. You will be spending roughly a week to do the following:

## Important Notes: 

PLEASE DO NOT COMMIT TO MAIN. Each one of these parts should be you creating ONE new branch + pull request (PR) in your repository. Ideally, each of your commits should also encompass roughly 1-3 of the bullet points specified for each part. After each one of these parts, please create an PR and assign me as the reviewer. I will read over your code and provide comments if necessary. 

The exact details of this project are largely omitted, so you will be tasked with designing some of the more granular features like the function headers, parameters, file structure, etc. In the review, I will mainly be looking to see if you have followed the part instructions, completed the deliverables (if provided), and maintained clean code formatting and structure.

## Part 1: FastAPI Basics (1-2 days)

Learn the basics of REST architecture (GET, POST, PATCH, DELETE, etc.). Learn why each method is important, where they can be used, and the benefits of using REST architecture.

Deliverables:
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

## Part 2: sqlalchemy/PostgreSQL basics (2-3 days)

We will now upgrade your crappy data structure to a database! All information that users can add and query will now be pulled from the database by the end of this part.

- Import sqlalchemy
- Setup a database using postgreSQL + sqlalchemy.
- Update your endpoints in parts 1 and 2 to actually do inserts into the database tables you created.
- Update your endpoints in parts 1 and 2 to require passing through user IDs.
- Create two tables, one for classes and another for users. Each class should include the following fields: class name, class name aliases, subject tags, prerequisites, students enrolled, max enrollment number, minimum grade level. Each user should include their name, admin level (restricted only to three increasing levels - "student", "instructor", and "admin"), enrolled classes, and published classes.
- You can use the psql command-line interface (CLI) to query and add to your databases. Alternatively, you can use the postgreSQL app manager, but I find this to be quite slow at times. To enter the CLI, use a command similar to below:
```bash
psql postgres -d [database_name]
```

Deliverables:
- Have a script that prepopulates the classes table in your database with 6 premade classes. You can set the owner of these classes to be some universal or global admin.
- Create a GET endpoint to retrieve all current users, their IDs, and any other relevant information.
- Create a GET endpoint that allows users to search for other users of similar grade level.
- Create a GET endpoint that allows users to search for other users that want to take the same class(es).
- Create a PATCH endpoint to allow users to update the current classes that they have taken. This will serve as determining if the prerequisite requirement has been met during enrollment in the next part.
- Create a POST endpoint that allows you to add a new user alongside their level (student, instructor, admin). This should also append to the database.
- Create a POST endpoint that allows users of the admin level to change other users' levels as long as they are not admins.
- Create a DELETE endpoint that allows students to remove a class they previously enrolled for.
- Update your DELETE endpoint to delete classes and users from their respective tables inside the database. Modify this endpoint so that only users of instructor level or above can use it.
- Create a mysterious user named "Paul Elliot" that has a 1% chance of instantly appearing in your classes whenever a user successfully enrolls. He will also add a prerequisite to the class called "Ping Pong."
- In general, after this part, all actions should now fetch and modify info from the setup database.

## Part 3: FastAPI + Pydantic (1-2 days)

This part introduces the world of schemas into the API! Pydantic allows you to ensure data sent into your API fits a certain standard and/or format. If a bad actor is to use your API, they are prevented from sending in bad requests. Adding schemas also makes it easier on the frontend/client side to know what to expect from backend APIs.

- Import Pydantic into your project repo.
- If not done already, formalize the school class object.
- Upgrade your API to take in specific simple schemas you've built from pydantic (at least 3 fields) and provide specified output schemas. Use Pydantic validators to do simpmle sanity checks for nonnegative enrollment numbers, grade levels to be in between 1-12, class name to be capped at a certain number of characters, and user names to be capped at a certain number of characters. By the end of this part, each endpoint should take in a pydantic schema and return some other schema, and have validators where appropraite.
- Add a new user schema that includes their name, admin level (restricted only to three increasing levels - "student", "instructor", "admin"), and optionally the classes taught.

Deliverables:
- Each endpoint refactored to input a schema and output another schema. Some schemas should have validators where appropriate.
- Update the GET endpoint that retrieves class information by name to also showcase the names of students enrolled and the number of students enrolled. This information should be restricted only to be of instructor level or higher. 
- To add a class, users now must be at least an instructor level. You should check this by checking what is passed through the POST endpoint's header. 
- Add a feature where instructors of a class can invite any other user, regardless of level, to be a co-instructor.
- Update the PATCH endpoint for changing class description + metadata so that it can only be done by the creator of the class and co-instructors.
- Create a feature where students can enroll in classes. Make sure to check the prerequisites.

## Part 4: Meet all deliverables criteria

- Allow a user to view the description and prerequisites of a specific class after sending a request containing the class name and user ID. If the user is an instructor, allow the user to see what students have signed up for the class they have posted.
- If the user is an instructor, allow this user to create a class that provides information of: class name, class name aliases, subject tags, prerequisites, students enrolled, max enrollment number, minimum grade level.
- Users should be able to search for classes based on various inputted tags. The result from the search should be classes that include all the inputted tags.

- Eric TODO : Add more deliverables