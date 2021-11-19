
from django.views import generic

"""from .forms import SchoolForm
from .models import School


class SchoolCreateView(generic.CreateView):
    model = School
    template_name = 'school_app.html'
    form_class = SchoolForm
    success_url = '/school_app/create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_app'] = School.objects.all()
        return context"""