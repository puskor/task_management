from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import Task_forms
from tasks.models import Employee

# Create your views here.

def manager(request):
    return render(request,"dashboard/manager.html")

def user(request):
    return render(request,"dashboard/user.html")

def test(request):
    return render(request,"test.html")

def create_task(request):
    employee=Employee.objects.all()
    form=Task_forms(employees=employee)
    context={"form":form}
    return render(request,"task_form.html",context)