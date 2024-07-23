# it-company-task-manager

The IT Company Task Manager is a comprehensive web application designed to help IT
companies manage their tasks, workers, and projects efficiently. 
This application provides features for task assignment, worker registration, task 
tracking, and more, ensuring seamless collaboration and productivity within the 
organization.

## Check it out

[Library project deployed to render](https://it-company-task-manager-id1m.onrender.com/)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Andrii1000/it-company-task-manager
cd taskManager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
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

## Demo
![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)



