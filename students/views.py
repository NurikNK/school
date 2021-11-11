from django.views import generic

from .forms import StudentForm, StudentCourseForm
from .models import Student, StudentCourse


class StudentCreateView(generic.CreateView):
    model = Student
    template_name = 'student.html'
    form_class = StudentForm
    success_url = 'home'


class StudentCourseCreateView(generic.CreateView):
    model = StudentCourse
    template_name = 'studentcourse.html'
    form_class = StudentCourseForm
    success_url = 'home'