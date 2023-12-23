
# 0x02. AirBnB Clone - MySQL | ALX Africa Intranet

## Overview

This project, 0x02. AirBnB Clone - MySQL, is part of the ALX Africa Intranet's ongoing second chance project. It focuses on developing an AirBnB clone using Python, OOP, and MySQL. The project aims to implement an Object-Relational Mapping (ORM) with SQLAlchemy, manage back-end development, handle SQL databases, and employ environment variables effectively.

### Team
- **Abdelali Laaguidi**
- **Mohamed Assouli**

## Project Details

### Learning Objectives
By the end of this project, the goals include understanding and implementing:
- Unit testing in large projects
- Usage of `*args` and `**kwargs`
- Handling named arguments in functions
- Creating and managing MySQL databases and users
- Mapping Python Classes to MySQL tables using ORM
- Handling different storage engines within the same codebase
- Effective utilization of environment variables

### Requirements
- **Python Scripts**
  - Usage of Ubuntu 20.04 LTS with Python3 (version 3.8.5)
  - Following PEP8 coding style guidelines
  - Extensive documentation in modules, classes, and functions
  - Execution of test files using the `unittest` module
- **SQL Scripts**
  - Execution on Ubuntu 20.04 LTS using MySQL 8.0 and SQLAlchemy version 1.4.x
  - Properly commented SQL queries and files
- **GitHub**
  - One project repository per group following specific guidelines

### Tasks Overview
The project comprises several tasks, including:
- Forking the existing codebase and updating the repository name
- Implementing bug-free unittests and PEP8 compliance
- Enhancing the console's functionality to allow object creation with given parameters
- Setting up MySQL databases for development and testing
- Implementing deletion of objects in the FileStorage engine
- Transitioning from FileStorage to DBStorage using SQLAlchemy

## Project Structure

### Files and Directories
- **`console.py`**: Handles command interpretation
- **`models/`**: Contains Python classes for the application models
- **`tests/`**: Includes all the unit test files
- **`setup_mysql_dev.sql`**: Script for preparing MySQL server for development
- **`setup_mysql_test.sql`**: Script for preparing MySQL server for testing
- **`models/engine/file_storage.py`**: Contains methods related to FileStorage engine

### Execution and Testing
- Unit tests canbe executed using `python3 -m unittest discover tests`
- Individual tests can be run using `python3 -m unittest tests/test_models/test_base_model.py`

## Conclusion

This project involves developing an AirBnB clone using Python, MySQL, and SQLAlchemy. It focuses on various aspects of back-end development, testing, SQL database management, and environment variable usage. The tasks range from forking the codebase to transitioning the storage engine from FileStorage to DBStorage using SQLAlchemy.

For more detailed information about each task and its execution, refer to the respective task files in the project repository.

---

Feel free to tailor this README file according to your specific project details, updates, and additional information as needed!
