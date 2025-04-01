from home.views import index
# from home.views import TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView
from home.views import TeacherListCreateView, TeacherDetailView
from home.views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

from django.urls import include, path

urlpatterns = [
    path('index/', index),
    # path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    # path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<str:student_id>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]
