# Todo List Web Application

This is a simple web application built with Django that allows users to manage their tasks.

## Features

- User authentication: Users can register, log in, and log out.
- Task management: Users can create, read, update, and delete tasks.
- Task filtering and search: Users can filter tasks based on completion status and search tasks by title.
- Task time scheduling: Users can schedule tasks with a specific time.
- Task notifications: Users receive notifications 3 hours before the scheduled time of their tasks.


Navigate to the project directory:
cd todo-list

Install the required dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Run the development server:
python manage.py runserver
