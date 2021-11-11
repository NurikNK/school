
from django.views import generic

from .forms import SchoolForm
from .models import School


class SchoolCreateView(generic.CreateView):
    model = School
    template_name = 'school_app.html'
    form_class = SchoolForm
    success_url = 'home'