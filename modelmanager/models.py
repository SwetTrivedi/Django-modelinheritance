from django.db import models
from .managers import CustomManager
# Create your models here.
class College(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField()
    # student=models.Manager()
    student=CustomManager()
     
