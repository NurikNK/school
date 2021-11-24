from rest_framework import serializers
from .models import Student, StudentCourse
import random


class StudentSerializer(serializers.ModelSerializer):
    average_score = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'school', 'is_active', 'is_graduated', 'average_score']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        student_courses = StudentCourse.objects.filter(student=instance)
        score, len_of_items = 0, 0
        for student_course in student_courses:
            score += student_course.score
            len_of_items += 1
        if len_of_items != 0:
            response['average_score'] = score / len_of_items
        return response

