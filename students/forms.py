from django.forms import ModelForm

from .models import Student, StudentCourse


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'date_of_birth',
            'school',
            'is_active',
            'is_graduated',
        ]


class StudentCourseForm(ModelForm):
    class Meta:
        model = StudentCourse
        fields = [
            'student',
            'course'
        ]


class StudentListForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'date_of_birth',
            'school',
            'is_active',
            'is_graduated',
        ]