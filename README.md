# it-company-task-manager

The IT Company Task Manager is a comprehensive web application designed to help IT
companies manage their tasks, workers, and projects efficiently. 
This application provides features for task assignment, worker registration, task 
tracking, and more, ensuring seamless collaboration and productivity within the 
organization.

## Check it out

[Library project deployed to render](https://it-company-task-manager-id1m.onrender.com/)

You can evaluate different functionality of this project by logining to different user entities:
```
user: test.user
password: 1qwerty2
```

## Features

* Worker Management:

Registration: Allows new workers to register and join the system.
Profile Management: Workers can update their profiles, including position details and personal information.
Search and Filter: Easily search for workers based on various criteria such as username.

* Task Management:

Creation and Assignment: Create tasks and assign them to multiple workers.
Task Types and Priorities: Define different task types and set priorities to manage task importance.
Task Status: Track whether tasks are completed or not.
Search and Filter: Search for tasks based on their name.

## Technologies Used
- Python
- Django
- Django Crispy Forms
- Bootstrap
- SQLite (default, can be replaced with PostgreSQL, MySQL, etc.)

## Installation

Python3 must be already installed

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd it-company-task-manager
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Demo
![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)



