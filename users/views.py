from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm,CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def sign_up(request):
    if request.method == "GET":
        form= CustomRegisterForm()
        
    if request.method =="POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request,"successfully SIGN UP")
            return redirect('home')
            
    context={
        "form":form
    }
    return render(request,"registrations/register.html",context)

def sign_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        print(username,password)
        user=authenticate(request,username=username ,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("home")
    return render(request,"registrations/sign_in.html")

def sign_out(request):
    if request.method=="POST":
        logout(request)
        return redirect("sign_in")
            
