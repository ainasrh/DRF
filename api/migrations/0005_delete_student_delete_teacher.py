# Generated by Django 5.1.3 on 2024-12-05 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_student_name_remove_student_place_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
