from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm,CustomRegisterForm,AssignRoleForm
from django.contrib import messages
from users.forms import LoginForm
from django.db.models import Prefetch
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User,Group



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
    
    
def admin_dashboard(request):
    users=User.objects.all()
    # users=User.objects.prefetch_related(
    #     Prefetch('groups',queryset=Group.objects.all(),to_attr="all_groups")
    # ).all()
    return render(request,"admin/dashboard.html",{"users":users})



def assign_role(request,user_id):
    user=User.objects.get(id=user_id)
    form=AssignRoleForm()
    if request.method=="POST":
        form=AssignRoleForm(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin-dashboard')
        
    return render(request,"admin/assign_role.html",{"form":form})
        