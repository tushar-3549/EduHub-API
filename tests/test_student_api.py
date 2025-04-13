# tests/test_student_api.py
import pytest
from rest_framework.test import APIClient
from home.factories import StudentFactory

@pytest.mark.django_db
def test_student_list_api_returns_existing_student():
    student = StudentFactory(email="tushar15-3549@diu.edu.bd")

    client = APIClient()
    response = client.get("/api/students/")
    
    assert response.status_code == 200
    data = response.json()
    emails = [item["email"] for item in data]
    
    assert student.email in emails
