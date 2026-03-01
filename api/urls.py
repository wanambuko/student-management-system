from django.urls import path
from .views import (
    MyTokenObtainPairView,
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    CourseListCreateView,
    EnrollmentListCreateView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # JWT Authentication
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Student endpoints
    path('students/', StudentListCreateView.as_view(), name='student_list_create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student_detail'),

    # Course endpoints
    path('courses/', CourseListCreateView.as_view(), name='course_list_create'),

    # Enrollment endpoints
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment_list_create'),
]