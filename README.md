## Edu-Hub API 

### Project Overview
The Edu-Hub API is a web-based application built with Django REST Framework (DRF) that facilitates CRUD operations for managing teachers, students, and courses. The admin is able to assign courses to teachers, and JWT authentication is used for secure access to the API endpoints. The project also incorporates pagination for the student API endpoint, and it is designed to be deployed using Docker and Docker Compose for efficient containerized management.

### Features
- CRUD Operations: Create, Read, Update, and Delete operations for teachers and students.
- Course Assignment: Admin can assign courses to teachers.
- Pagination: Pagination added to the students' API endpoint for optimized data fetching.
- JWT Authentication: Secure access to API endpoints using JSON Web Tokens (JWT).
- Docker Deployment: Includes a Dockerfile and Docker Compose yaml configuration for easy deployment and containerization.
- Database: Utilizes the default SQLite3 database for storing data.

### Tech Stack
- Backend: Django REST Framework
- Database: SQLite3 (default database)
- Security: JWT Authentication
- Version Control: Git & GitHub
- Containerization: Docker & Docker Compose

### Installation Instructions

To set up and run the Edu-Hub API project locally, follow these steps:

 - Clone the Repository

```git clone https://github.com/yourusername/edu-hub-api.git
   cd edu-hub-api
```


### ER Diagram:

+------------+      1      +------------+      *      +------------+
|  Course    | <---------> |  Teacher   | <---------> |  Student   |
+------------+             +------------+             +------------+
| course_code| PK          | teacher_id | PK          | student_id | PK
| title      |            | name       |            | f_name     |
| duration   |            | phone      |            | l_name     |
+------------+            | hire_date  |            | sur_name   |
                          | salary     |            | email      |
                          | is_active  |            | dept       |
                          | course_id  | FK         | address    |
                          +------------+            +------------+

User Authentication:
+------------+
|   User     |
+------------+
| username   |
| email      |
| password   |
+------------+


### Set Up the Virtual Environment

```python3 -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate  # For Windows
```

### Install Dependencies

`pip install -r requirements.txt`

### Run Migrations

`python manage.py migrate`

### Create a Superuser (for admin access)

`python manage.py createsuperuser`

### Run the Development Server

    `python manage.py runserver`

    - Access the API

    Open your browser and go to `http://127.0.0.1:8000/` to access the API endpoints.

