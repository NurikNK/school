from django.contrib.auth.models import User
from rest_framework import serializers, validators
from employees.models import Employee, Position


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=True, min_length=8)
    date_of_birth = serializers.DateField(write_only=True)
    image = serializers.ImageField(write_only=True, required=False, allow_null=True)
    position = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Position.objects.all())
    salary = serializers.DecimalField(write_only=True, max_digits=7, decimal_places=2)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs['password']
        confirm_password = attrs['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(detail='password does not match', code='password_match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        Employee.objects.create(
            user=user,
            date_of_birth=validated_data['date_of_birth'],
            image=validated_data['image'],
            position=validated_data['position'],
            salary=validated_data['salary'],
        )
        return user
