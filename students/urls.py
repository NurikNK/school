from django.urls import path

from .views import StudentCreateView, StudentCourseCreateView, student_list, students_detail, StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    # path('create/', StudentCreateView.as_view()),
    path('students/', StudentListAPIView.as_view(), name="students-list"),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name="students-detail"),
    path('student_course_create/', StudentCourseCreateView.as_view()),

]

