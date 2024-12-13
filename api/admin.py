from django.contrib import admin
from .models import student,teacher
# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','place']
@admin.register(teacher)
class TeacherDisplay(admin.ModelAdmin):
    list_display=['name','age']    
