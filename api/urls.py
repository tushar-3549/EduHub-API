# from home.views import index, login
# from home.views import TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView
from home.views import TeacherListCreateView, TeacherDetailView
from home.views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

from django.urls import include, path

from home.views import index, login_view  
from rest_framework_simplejwt.views import TokenRefreshView
from home.views import register_view, login_view

urlpatterns = [
    path('index/', index),

    # path('login/', login),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    # path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<str:student_id>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
]
