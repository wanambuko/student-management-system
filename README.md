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
# 1. Clone the repository
git clone <your-repo-link>

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply migrations
python manage.py migrate

# 6. Run server
python manage.py runserver