from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import Task_forms
from tasks.models import Employee,Task

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
    
    if request.method=="POST":
        form = Task_forms(request.POST,employees=employee)
        if form.is_valid():
            data=form.cleaned_data
            title=data.get("title")
            description=data.get("description")
            due_date=data.get("due_date")
            employee=data.get("employee")
            
            task=Task.objects.create(title=title,description=description,due_date=due_date)
        
            for emp_id in employee:
                emp=Employee.objects.get(id=emp_id)
                task.employee.add(emp)
                
        
        
    context={"form":form}
    return render(request,"task_form.html",context)