from django.shortcuts import render
from .models import College
# Create your views here.
def college(request):
    student_data=College.student.all()
    student_data=College.student.get_roll_range(101,103)
    return render(request,'college.html',{'students':student_data})