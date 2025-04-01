from django.urls import path
from tasks.views import manager,user,test,create_task,view_task,update_task,delete_task

# from tasks.templates.dashboard import dashboard



urlpatterns = [
    path("manager/",manager,name="manager"),
    path("user/",user,name="user"),
    path("test/",test),
    path("create_task/",create_task,name="create_task"),
    path("view_task/",view_task),
    path("update_task/<int:id>/",update_task,name="update_task"),
    path("delete_task/<int:id>/",delete_task,name="delete_task")
]
