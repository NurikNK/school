from django.views import generic

from .forms import StudentForm, StudentCourseForm, StudentListForm
from .models import Student, StudentCourse
from django.views.generic import ListView


"""class StudentListView(ListView):
    model = Student
    template_name = 'student_index.html'
    form_class = StudentListForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['students'] = Student.objects.all()
        return context"""


class StudentCreateView(generic.CreateView):
    model = Student
    template_name = 'student.html'
    form_class = StudentForm
    success_url = '/students/create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context


class StudentCourseCreateView(generic.CreateView):
    model = StudentCourse
    template_name = 'studentcourse.html'
    form_class = StudentCourseForm
    success_url = '/students/student_course_create/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_course'] = StudentCourse.objects.all()
        return context