from rest_framework import serializers
from .models import Teacher, Student, Course


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = ['course_code', 'course_title', 'duration']

class TeacherSerializer(serializers.ModelSerializer):
    taken_course = CourseSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'
        # depth = 1


class NameSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=50)
    l_name = serializers.CharField(max_length=50)
    sur_name = serializers.CharField(max_length=30, required=False, allow_null=True)

class StudentSerializer(serializers.ModelSerializer):
    name = NameSerializer(source='*')  # Use '*' to include all the relevant fields in the name serializer

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'dept', 'address']

    def get_name(self, obj):
        return {
            "f_name": obj.f_name,
            "l_name": obj.l_name,
            "sur_name": obj.sur_name
        }
