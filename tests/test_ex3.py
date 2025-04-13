import pytest
from home.models import Course, Teacher, Student
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_course():
    course = Course.objects.create(course_code='CSE201', course_title='C Programming', duration='3 months')
    assert str(course) == 'CSE201'

@pytest.mark.django_db
def test_teacher():
    course = Course.objects.create(course_code='CSE201', course_title='C Programming', duration='3 months')
    teacher = Teacher.objects.create(teacher_id='1', teacher_name='Mohammad Ali', taken_course=course)
    assert str(teacher) == 'Mohammad Ali'

@pytest.mark.django_db
def test_student():
    student = Student.objects.create(
        student_id='S01', f_name='Alice', l_name='Smith', email='alice@example.com', dept='CSE', address='Dhaka'
    )
    assert str(student) == 'Alice Smith'


# @pytest.mark.django_db
# def test_existing_student_in_api():
#     client = APIClient()
#     response = client.get('/api/students/') 
#     assert response.status_code == 200
#     data = response.json()
#     target_email = 'tushar15-3549@diu.edu.bd'  
#     found = any(student['email'] == target_email for student in data)
#     assert found, f"Student with email {target_email} not found in API"