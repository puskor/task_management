from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manager(request):
    return render(request,"dashboard/manager.html")

def user(request):
    return render(request,"dashboard/user.html")


def test(request):
    return HttpResponse("hello")