# M.E.A.L. (DFECLOUD7) Final Project

### Resources:
* Demo Video - M.E.A.L. - Meal Planning App: https://drive.google.com/file/d/1C-PNlIIp3dUqBgtgkEwMfYz5DEnzWZqc/view?usp=sharing

## Contents
* [Brief](#brief)
   * [Application](#application)
   * [Database](#database)
   * [Testing](#testing)
* [Technologies](#technologies)
* [The Project](#theproject)

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
* Project tracking: Jira
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


