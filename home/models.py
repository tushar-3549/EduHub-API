from django.db import models

# Create your models here.


class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_title = models.CharField(max_length=20)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_code
    

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, unique=True)
    teacher_name = models.CharField(max_length=50)
    taken_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='taken_course')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True) 
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    sur_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=30)
    dept = models.CharField(max_length=30, null=False)
    address = models.TextField()


    def __str__(self):
        return f"{self.f_name} {self.l_name}"

