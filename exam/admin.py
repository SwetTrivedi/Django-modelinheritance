from django.contrib import admin
from . models import ExamCenter,Student_exam
# Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']

@admin.register(Student_exam)
class Student_examAdmin(admin.ModelAdmin):
    list_display=['id','cname','city','name','roll']
