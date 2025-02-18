from django.shortcuts import render
from . models import ExamCenter, MyExamCenter

# Create your views here.
def prox (request):
    examcenter_data=ExamCenter.objects.all()
    myexamcenter_data=MyExamCenter.objects.all()
    return render (request,'prox.html',{'examcenters':examcenter_data,
                                        'myexamcenters':myexamcenter_data})