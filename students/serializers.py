from rest_framework import serializers
from .models import Student, StudentCourse
from schools_app.models import School


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    is_active = serializers.BooleanField(default=False)
    is_graduated = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """create() method creates and returns a new Course instance"""
        """Course.objects.create(**validated_data)"""

        student = Student.objects.create(
            name=validated_data['name'],
            date_of_birth=validated_data['date_of_birth'],
            school=validated_data['school'],
            is_active=validated_data['is_active'],
            is_graduated=validated_data['is_graduated'],
        )
        return student

    def update(self, instance, validated_data):
        """
        Update and return existing instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.school = validated_data.get('school', instance.school)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_graduated = validated_data.get('is_graduated', instance.is_graduated)
        instance.save()
        return instance