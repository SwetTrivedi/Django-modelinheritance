from django.contrib import admin
from .models import College
# Register your models here.

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display=['id','name','roll']