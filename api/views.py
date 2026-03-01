from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer


# Custom token view for admin login
class MyTokenObtainPairView(TokenObtainPairView):
    pass


# --------------------
# Student Views
# --------------------
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in admin can access


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


# --------------------
# Course Views
# --------------------
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


# --------------------
# Enrollment Views
# --------------------
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        student_id = request.data.get("student")
        course_id = request.data.get("course")

        # Validate that student and course exist
        if not student_id or not course_id:
            return Response(
                {"detail": "Both 'student' and 'course' fields are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check for duplicate enrollment
        if Enrollment.objects.filter(student_id=student_id, course_id=course_id).exists():
            return Response(
                {"detail": "This student is already enrolled in the selected course."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # If validation passes, proceed to create enrollment
        return super().create(request, *args, **kwargs)