import factory
from django.contrib.auth.models import User
from home.models import Student

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'defaultpass123')


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    student_id = factory.Sequence(lambda n: f"S{n:04}")
    f_name = "Test"
    l_name = "Student"
    email = factory.LazyAttribute(lambda obj: f"{obj.student_id.lower()}@test.com")
    dept = "CSE"
    address = "Test Address"
