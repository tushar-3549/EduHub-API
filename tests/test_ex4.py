import pytest
from rest_framework.test import APIClient
from home.models import Student

@pytest.mark.django_db
@pytest.mark.parametrize("student_data", [
    {
        "student_id": "3549",
        "f_name": "",
        "l_name": "",
        "sur_name": None,
        "email": "tushar15-3549@diu.edu.bd",
        "dept": "CSE",
        "address": "Tangail Sadar, Tangail"
    },
    {
        "student_id": "3353",
        "f_name": "Md Emam",
        "l_name": "Shafi",
        "sur_name": "Shafi",
        "email": "emam15-3353@diu.edu.bd",
        "dept": "BBA",
        "address": "Natore, Bangladesh"
    },
    {
        "student_id": "2134",
        "f_name": "Md Milon",
        "l_name": "Mia",
        "sur_name": "Milon",
        "email": "milon15-2134@diu.edu.bd",
        "dept": "Digital Marketing",
        "address": "Barishal, Bangladesh"
    },
])
def test_student_in_api(student_data):
    Student.objects.create(**student_data)

    client = APIClient()
    response = client.get('/api/students/')  

    assert response.status_code == 200

    data = response.json()

    found = any(student['email'] == student_data['email'] for student in data)

    assert found, f"Student with email {student_data['email']} not found in API"
