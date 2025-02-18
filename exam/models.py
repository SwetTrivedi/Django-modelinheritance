from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)


class Student_exam(ExamCenter):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
