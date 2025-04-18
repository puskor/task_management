from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm,CustomRegisterForm
from django.contrib import messages
from users.forms import LoginForm

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User



# Create your views here.

def sign_up(request):
    form= CustomRegisterForm()
    if request.method =="POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.is_active=False
            user.save()
            messages.success(request,"successfully SIGN UP")
            return redirect('sign_in')
            
    context={
        "form":form
    }
    return render(request,"registrations/register.html",context)


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("hello")
            return redirect('home')
    # return render(request, 'registrations/sign_in.html', {'form': form})
    return redirect("home")


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign_in')


def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            print(token)
            user.is_active = True
            user.save()
            return redirect('sign_in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')