# AirBnB clone

## The Console
This project is a simplified clone of the AirBnB web application. It includes a command interpreter that allows users to interact with the application through a command-line interface (CLI). The command interpreter can create, read, update, and delete objects, as well as manage serialization and deserialization of instances.

## Getting Started
### Prerequisites
Make sure you have Python 3.x installed on your system.

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/AirBnB_clone.git
    ```
2. Navigate to the project directory:
    ```sh
    cd AirBnB_clone
    ```
3. Make the console executable:
    ```sh
    chmod +x console.py
    ```

## Usage
### How to Start the Console
To start the console, run the following command from the project directory:
```sh
./console.py
```

### The console supports the following commands:

- quit or EOF: Exit the console.
- create <class_name>: Create a new instance of a class.
- show <class_name> <id>: Display the string representation of an instance based on its class name and id.
- destroy <class_name> <id>: Delete an instance based on its class name and id.
- all [<class_name>]: Display the string representation of all instances, optionally filtered by a class name.
- update <class_name> <id> <attribute_name> <attribute_value>: Update an instance based on its class name and id by adding or updating an attribute.

## Examples
### Here are some examples of how to use the console:
1- Starting the console:
```sh
./console.py
(hbnb)
```
2- Creating a new User instance:
```sh
(hbnb) create User
4ec40f93-8e5a-4abe-b7aa-2b98570c6542
```
3- Showing an instance:
```sh
(hbnb) show User 4ec40f93-8e5a-4abe-b7aa-2b98570c6542
[User] (4ec40f93-8e5a-4abe-b7aa-2b98570c6542) {'id': '4ec40f93-8e5a-4abe-b7aa-2b98570c6542', 'created_at': datetime.datetime(2024, 5, 19, 23, 49, 54, 824964), 'updated_at': datetime.datetime(2024, 5, 19, 23, 49, 54, 824989)}
```
4- Updating an instance:
```sh
(hbnb) update User 4ec40f93-8e5a-4abe-b7aa-2b98570c6542 email "example@example.com"
```
5- Destroying an instance:
```sh
(hbnb) destroy User 4ec40f93-8e5a-4abe-b7aa-2b98570c6542
```
6- Showing all instances:
```sh
(hbnb) all User
[]
```
7- Exiting the console:
```sh
(hbnb) quit
```

## General learning objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
