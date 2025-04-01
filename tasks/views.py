from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import Task_forms,Task_model_form,TaskDetailModelForm
from tasks.models import Employee,Task
from django.db.models import Q,Count,Max,Min,Avg
from django.contrib import messages

# Create your views here.

def manager(request):
    
    # total_task=tasks.count()
    # pending_task=Task.objects.filter(status="PENDING").count()
    # completed_task=Task.objects.filter(status="COMPLETED").count()
    # to_do=Task.objects.filter(status="IN_PROGRESS").count()
    counts=Task.objects.aggregate(
        total=Count("id"),
        completed=Count("id",filter=Q(status="COMPLETED")),
        pending=Count("id",filter=Q(status="PENDING")),
        to_do=Count("id",filter=Q(status="IN_PROGRESS"))
    )
    type=request.GET.get("type","all")
    base_query=Task.objects.select_related("details").prefetch_related("assigned_to")
    # tasks=base_query.all()
  
    if type=="completed":
        tasks=base_query.filter(status="COMPLETED")
    elif type=="pending":
        tasks=base_query.filter(status="PENDING")
    elif type=="to_do":
        tasks=base_query.filter(status="IN_PROGRESS")
    elif type=="all":
        tasks=base_query.all()
    
    context={
        "tasks":tasks,
        "counts":counts
    }
    
    return render(request,"dashboard/manager.html",context)

def user(request):
    return render(request,"dashboard/user.html")

def test(request):
    return render(request,"test.html")

def create_task(request):
    # employee=Employee.objects.all()
    task_form=Task_model_form()
    task_detail_form=TaskDetailModelForm()
    
    if request.method=="POST":
        task_form=Task_model_form(request.POST)
        task_detail_form=TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task=task_form.save()
            task_detail=task_detail_form.save(commit=False)
            task_detail.task=task
            task_detail.save()
            
            messages.success(request,"TASK CREATE SUCCESSFULLY")
            return redirect("create_task")
    
    context={"task_form":task_form,"task_detail_form":task_detail_form}
    return render(request,"task_form.html",context)


def update_task(request,id):
    # employee=Employee.objects.all()
    task=Task.objects.get(id=id)
    task_form=Task_model_form(instance=task)
    if task.details:
        task_detail_form=TaskDetailModelForm(instance=task.details)
   
    
    if request.method=="POST":
        task_form=Task_model_form(request.POST,instance=task)
        task_detail_form=TaskDetailModelForm(request.POST,instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():
            task_form.save()
            task_detail_form.save()
            
            messages.success(request,"TASK UPDATE SUCCESSFULLY")
            return redirect("update_task",id)
    
    context={"task_form":task_form,"task_detail_form":task_detail_form}
    return render(request,"task_form.html",context)


def delete_task(request,id):
    if request.method=="POST":
        task=Task.objects.get(id=id)
        task.delete()
        messages.success(request,"Delete successfully ")
        return redirect("manager")
    else:
        messages.error(request,"something is error")
        return redirect("manager")
        






def view_task(request):
    
    """get and filter checking """
    # tasks=Task.objects.all()
    tasks=Task.objects.select_related("details").all()
    
    
    # tasks=Task.objects.get(status="PENDING")
    # tasks=Task.objects.filter(status="PENDING")
    return render(request,"view_task.html",{"tasks":tasks})
