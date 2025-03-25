from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=50)
    start_date=models.DateField()
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)

class Task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    employee=models.ManyToManyField(Employee)
    title=models.CharField(max_length=150)
    description=models.TextField()
    due_date=models.DateField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    
class Task_details(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OPTIONS=(
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
    # Task is parent
    task=models.OneToOneField(Task,on_delete=models.CASCADE)
    assignd_to=models.CharField(max_length=50)
    priority=models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default=LOW)