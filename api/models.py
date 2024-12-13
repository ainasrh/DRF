from django.db import models

# Create your models here.


class teacher(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField() 

    def __str__(self):
        return self.name   

class student(models.Model):
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.name  
        