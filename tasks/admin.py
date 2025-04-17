from django.contrib import admin

# Register your models here.

from tasks.models import Task,Task_details,Employee,Project

admin.site.register(Task)
admin.site.register(Task_details)
admin.site.register(Employee)
admin.site.register(Project)

