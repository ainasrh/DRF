# Generated by Django 5.1.3 on 2024-12-05 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='place',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
    ]