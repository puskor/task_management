from django.db import models

# Create your models here.


class Task(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    due_date=models.DateField(auto_now=False, auto_now_add=False)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=False)
    
    
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