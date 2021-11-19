from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    # path('students/', include('students.urls')),
    # path('school_app/', include('schools_app.urls')),
]
