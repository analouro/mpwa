# M.E.A.L. (DFECLOUD7) Final Project

### Resources:
* Demo Video - M.E.A.L. - Meal Planning App: https://drive.google.com/file/d/1C-PNlIIp3dUqBgtgkEwMfYz5DEnzWZqc/view?usp=sharing
* MoSCoW file - https://github.com/analouro/mpwa/blob/824f26c192371ae5e9a04681b25a5d7bf86c1ad7/moscow.txt
* Entity Relationship Diagram (ERD) - https://github.com/analouro/mpwa/blob/824f26c192371ae5e9a04681b25a5d7bf86c1ad7/MPWA-ERD.drawio

## Contents
* [Brief](#brief)
   * [Application](#application)
   * [Database](#database)
   * [Testing](#testing)
* [Technologies](#technologies)
* [The Project](#theproject)
* [Structure](#structure)

## Brief
This project has the following objectives:
1. To create a web application that integrates with a database and demonstrates CRUD functionality;
2. To utilise containers to host and deploy your application;
3. To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.

## Application
Requirements:
1. Monolithic Flask application - serves backend and frontend;
2. Frontend uses HTML templates;
3. The application most demonstrate CRUD functionality with information from the database;
4. The application most use SQLAlchemy to model and integrate with the database.

## Database
Requirements:
1. The application must interface with a separate database service;
2. The database must contain two tables with a relationship;
3. The relationship must at least be one-to-many.

# Testing
Requirements:
1. Unit tests must be written for the application with the aim of achieving high coverage (at least 75%).

## Technologies
Here is a list of all the technologies used in this project and correspondent purposes:
* Jira: Project tracking
* Git: Version Control
* GitHub: Code Repository
* Python: Programming language
* Pytest: Unit-Tests
* Flask: Micro web framework (Python)
* MySQL: Open source relational database
* Docker/Docker Compose: Open source containerization platform
* Docker Hub: Container image library
* Docker Swarm: Container orchestration tool

## The Project
In order to achieve the goals established in the project brief, and because of my background in Nutrition, I decided to not only create something to achieve the goal but also something that could have a purpose in "the real world". Based on a professional project of mine, I created M.E.A.L. (make eating about love), a meal planning application that can be used to generate meal plans for families.

I have delivered the MVP (as shown in the Demo Video), that allows a user to:
1. Create a new user (name);
2. Create a new recipe (name);
3. Read all the users and recipes;
4. Update the name of a recipe;
5. Delete a recipe;
6. Generate a random 5 day meal plan using the recipe "library".

Next stages of development (user stories that were included into the project's Jira backlog but were not added in this MVP stage):
* Add ingredients to a recipe;
* Add servings to a recipe;
* Add instructions to a recipe;
* Delete users;
* Read recipes from a specific user.

*The user stories chosen for the MVP were defined using the MoSCoW prioritisation and estimations of efforts as can be observed in the file moscow.txt

## Structure

* Database:
The database has two tables (User and Recipe) that form a one-to-many relationship.
The one-to-many relationship allows each user to add several recipes, but each recipe belongs only to one user.

![ERD-Model](https://user-images.githubusercontent.com/97620020/157756704-0569f552-6cc9-4120-a2f6-49af07ce6984.png)

![mysql - user and recipe table](https://user-images.githubusercontent.com/97620020/157757024-fac5ff09-6c26-4ff6-9a4b-5c6bb722bfaf.png)

* CI/CD Pipeline:

**CI (Continuous Integration):** Enables constant update and testing of code.
  * In this project the Project Tracking Tool was integrated into GitHub, however, the commands were not functioning correctly, therefore the Project Tracking Tool was used manually (which isn't ideal and is something that needs to be corrected in the future).
  * GitHub was used as the code repository - new branches were created for each sprint ("MPWA-3" (deleted from GitHub) to develop user stories related to the user, "MPWA-4" to develop user stories related to recipes, "unit-tests" to develop unit-tests).
  * CI Server: Jenkins was used to build and test the code created - this was achieved by writing a Jenkins pipeline job with separate stages (scripts):
    1. Declarative: Checkout SCM
    2. Fetch Git Repository
    3. Setup
    4. Test
    5. Build
  



--insert image--





