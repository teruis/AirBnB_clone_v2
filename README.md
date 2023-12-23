**Overview**

This project is the first step in building a fully functional AirBnB clone web application. It involves creating a command-line interface to manage AirBnB objects using the cmd module in Python.

**Learning Objectives**

By completing this project, you will be able to:

* Understand the concept of Python packages
* Create a command-line interface using the cmd module
* Implement unit testing to ensure code quality
* Serialize and deserialize Python objects
* Work with JSON files and manage datetime objects

**Tasks**

1. Create a README.md file and an AUTHORS file
2. Ensure your code complies with pep8 style guidelines
3. Implement unit tests for all modules, classes, and functions
4. Create a BaseModel class with common attributes and methods
5. Add functionality to recreate a class instance from a dictionary representation
6. Implement a FileStorage class to manage persistent file storage
7. Update the console with basic functionality to quit, handle empty lines and ^D
8. Add methods to create, destroy, show, and update stored data
9. Create additional classes for User, Place, City, Amenity, State, and Review
10. Update the console and file storage system to handle all classes dynamically

**Running the Console**

1. Clone the repository
2. Locate the "console.py" file
3. Run the file using the command: ./console.py
4. You will be prompted with the "(hbnb)" prompt

**Example Commands**

* **create BaseModel:** Creates a new BaseModel instance
* **show BaseModel <_id>:** Shows an existing BaseModel instance
* **destroy BaseModel <_id>:** Destroys an existing BaseModel instance
* **update BaseModel <_id> <attribute_name> <attribute_value>:** Updates an existing BaseModel instance
* **quit:** Exits the console

**Alternative Syntax**

You can use alternative syntax for some commands:

* **<class_name>.all():** Shows all objects of the given class
* **<class_name>.destroy(<_id>):** Destroys an existing object of the given class
* **<class_name>.update(<_id>, <attribute_name>, <attribute_value>):** Updates an existing object of the given class
* **<class_name>.update(<_id>, <dictionary>):** Updates an existing object of the given class using a dictionary of attribute-value pairs
