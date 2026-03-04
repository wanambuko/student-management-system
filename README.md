# Student Management System (Backend)

Capstone Project – Student Management System built using Django REST Framework.

## Features
- JWT Authentication (Admin login)
- Student CRUD API
- Course Management API
- Student Enrollment API
- Duplicate enrollment prevention

## Technologies Used
- Django
- Django REST Framework
- Simple JWT
- SQLite

## API Endpoints
- POST /api/login/
- POST /api/students/
- GET /api/students/
- PUT /api/students/{id}/
- DELETE /api/students/{id}/
- POST /api/courses/
- GET /api/courses/
- POST /api/enrollments/
- GET /api/enrollments/

## How to Run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver