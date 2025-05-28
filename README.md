## EduHub API - Django REST

#### Project Overview
The Edu-Hub API is a web-based application built with Django REST Framework (DRF) that facilitates CRUD operations for managing teachers, students, and courses. The admin is able to assign courses to teachers, and JWT authentication is used for secure access to the API endpoints. The project also incorporates pagination for the student API endpoint, and it is designed to be deployed using Docker and Docker Compose for efficient containerized management.

### 🚀 Features

   🔁 CRUD Operations: Create, Read, Update, and Delete teachers and students.

   📚 Course Assignment: Admin can assign multiple courses to teachers.

   📄 Pagination: Efficient pagination on the student endpoint for better performance.

   🔒 JWT Authentication: Secure access to API endpoints using JSON Web Tokens (JWT)

   🐳 Dockerized Deployment: Includes a Dockerfile and Docker Compose yaml configuration for easy deployment and containerization.

   🗃️ Database: Default support with SQLite3 for storing data

🛠️ ### Tech Stack
- Backend: Django REST Framework
- Database: SQLite3 (default database)
- Security: JWT Authentication
- Testing: Pytest, Postman
- Version Control: Git & GitHub
- Containerization: Docker & Docker Compose

### 📦 Installation & Setup

To set up and run the Edu-Hub API project locally, follow these steps:

1. Clone the Repository
  ```
     git clone https://github.com/tushar-3549/EduHub-API
     cd EduHub-API
  ```
2. Create & Activate Virtual Environment
   ```
   python3 -m venv venv
   
   source venv/bin/activate  (macOS/Linux)
   venv\Scripts\activate (windows)
   ```
3. Install Requirements
   ```
   pip install -r requirements.txt
   ```
4. Apply Migrations
   ```
   python manage.py migrate
   ```
5. Create Superuser
   ```
   python manage.py createsuperuser
   ```
6.  Run Development Server
   ```
   python manage.py runserver
   ```

- Open your browser and go to `http://127.0.0.1:8000/` to access the API endpoints.

### 🐳 Docker Setup

Make sure you have Docker and Docker Compose installed.
```
# Build and run the containers
docker-compose up --build
```
- Visit the API: `http://localhost:8000/`

### 🧪 Running Tests

To run tests using Pytest:
```
pytest
```

### ER Diagram: 

![Screenshot from 2025-05-28 19-36-28](https://github.com/user-attachments/assets/b79f4a8f-d206-43df-b4da-a735523fb9cb)

