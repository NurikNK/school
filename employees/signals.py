from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee
import json


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Employee)
def user_created(sender, instance, created, **kwargs):
    if created:
        employee_data = {
            'date_of_birth': str(instance.date_of_birth),
            'position': str(instance.position),
            'salary': str(instance.salary)
        }
        with open('employees.json', 'a') as file:
            file.write(json.dumps(employee_data, indent=4, sort_keys=True))

