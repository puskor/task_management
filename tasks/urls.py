from django.urls import path
from tasks.views import manager,user,test

# from tasks.templates.dashboard import dashboard



urlpatterns = [
    path("manager/",manager),
    path("user/",user),
    path("test/",test)
    
    
]
