from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TeacherSerializer, StudentSerializer, LoginSerializer
# from rest_framework import viewsets
from .models import Teacher, Student
from rest_framework import generics

from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Teacher

@api_view(['GET']) 
def index(request):
    return Response({"message": "Hello, Welcome to Tech-Hub API!"})

# class TeacherListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

# class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

@api_view(['POST'])
def login(request):
    data = request.data 
    serializer = LoginSerializer(data = data)

    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({"message": "success"})
    return Response(serializer.errors)



class TeacherListCreateView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        search_name = self.request.query_params.get('search', None)  # `search` query parameter ta niye aschi
        if search_name:
            queryset = queryset.filter(teacher_name__startswith=search_name) # teacher_name "m" diye start hole filter
        return queryset
       

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Teacher created successfully!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"message": "Teacher details fetched successfully!", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Teacher updated successfully!", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Teacher deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT
        )


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    lookup_field = 'student_id'