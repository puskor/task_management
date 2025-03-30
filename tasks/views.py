from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import Task_forms,Task_model_form
from tasks.models import Employee,Task
from django.db.models import Q

# Create your views here.

def manager(request):
    return render(request,"dashboard/manager.html")

def user(request):
    return render(request,"dashboard/user.html")

def test(request):
    return render(request,"test.html")

def create_task(request):
    # employee=Employee.objects.all()
    form=Task_model_form()
    
    if request.method=="POST":
        form = Task_model_form(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request,"task_form.html",{"form":form ,"message":"Adding is success"})
            # data=form.cleaned_data
            # title=data.get("title")
            # description=data.get("description")
            # due_date=data.get("due_date")
            # employee=data.get("employee")
            
            # task=Task.objects.create(title=title,description=description,due_date=due_date)
        
            # for emp_id in employee:
            #     emp=Employee.objects.get(id=emp_id)
            #     task.employee.add(emp)
            
            # return HttpResponse("success")
                
        
        
    context={"form":form}
    return render(request,"task_form.html",context)

def view_task(request):
    
    """get and filter checking """
    # tasks=Task.objects.all()
    tasks=Task.objects.select_related("project").all()
    
    
    # tasks=Task.objects.get(status="PENDING")
    # tasks=Task.objects.filter(status="PENDING")
    return render(request,"view_task.html",{"tasks":tasks})
