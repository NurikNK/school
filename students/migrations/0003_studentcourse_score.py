# Generated by Django 3.2.9 on 2021-11-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='score',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]