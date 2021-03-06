from rest_framework import serializers
from .models import Student, StudentCourse
import random
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class StudentSerializer(serializers.ModelSerializer):
    average_score = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'email', 'school', 'is_active', 'is_graduated', 'average_score']

    def create(self, validated_data):
        student = super().create(validated_data)
        subject = 'Hallo massage/do not reply'
        message = 'Welcome to our school'
        from_email = settings.EMAIL_HOST_USER
        to_list = [student.email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=True)
        return student

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

