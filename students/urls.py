from django.urls import path

from .views import StudentCreateView, StudentCourseCreateView

urlpatterns = [
    path('create/', StudentCreateView.as_view()),
    path('student_course_create/', StudentCourseCreateView.as_view()),

]