from django.urls import path

from .views import CourseCreateView, courses_list, courses_detail

urlpatterns = [
    # path('create/', CourseCreateView.as_view()),
    path('courses/', courses_list, name='course-list'),
    path('courses/<int:pk>/', courses_detail, name='course-detail'),
]