from django.urls import path
from tasks.views import manager,user,test,create_task

# from tasks.templates.dashboard import dashboard



urlpatterns = [
    path("manager/",manager),
    path("user/",user),
    path("test/",test),
    path("create_task/",create_task)
    
]
