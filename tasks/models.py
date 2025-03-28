from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateField()
    def __str__(self):
        return self.name
    
    
    
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    status_choices=[
        ('Pending',"Pending"),
        ('In_progress',"In_progress"),
        ('Completed',"Completed")
    ]
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    assigned_to=models.ManyToManyField(Employee)
    title=models.CharField(max_length=150)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=15,choices=status_choices,default="Pending")
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
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
    nodes=models.CharField(blank=True,null=True)
    
    def __str__(self):
        return f"Details from {self.task.title}"