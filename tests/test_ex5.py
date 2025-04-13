import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
@pytest.mark.parametrize("username, email, password", [
    ('tushar', 'tushar@gmail.com', 'tushar_12345'),
    ('maruf', 'maruf123@gmail.com', 'hello54321'), 
])
def test_user_registration(username, email, password):
    client = APIClient()
    
    payload = {
        "username": username,
        "email": email,
        "password": password
    }

    response = client.post("/api/register/", payload, format='json')

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    assert User.objects.filter(username=username).exists(), "User not created in DB"
