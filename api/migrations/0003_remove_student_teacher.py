# Generated by Django 5.1.3 on 2024-12-05 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_teacher_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]