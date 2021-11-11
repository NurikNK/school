from django.views import generic

from .forms import CourseForm
from .models import Course


class CourseCreateView(generic.CreateView):
    model = Course
    template_name = 'course.html'
    form_class = CourseForm
    success_url = 'home'



