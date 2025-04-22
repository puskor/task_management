from django.shortcuts import render,redirect,HttpResponse
from users.forms import RegisterForm,CustomRegisterForm,AssignRoleForm,Create_group_form
from django.contrib import messages
from users.forms import LoginForm
from django.db.models import Prefetch
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test


# Create your views here.

def is_admin(user):
    return user.groups.filter(name="Admin").exists()

def sign_up(request):
    form= CustomRegisterForm()
    if request.method =="POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get("password"))
            user.is_active=False
            user.save()
            messages.success(request,"Pleace check your mail")
            return redirect('sign_in')
            
    context={
        "form":form
    }
    return render(request,"registrations/register.html",context)


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("hone a acce ")
            return redirect('home')
    print("home a jay nai")
    return render(request, 'registrations/sign_in.html', {'form': form})

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('base')
    return redirect("sign_in")


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
    
@user_passes_test(is_admin, login_url='no_permission')
def admin_dashboard(request):
    users = User.objects.prefetch_related(
        Prefetch('groups', queryset=Group.objects.all(), to_attr='all_groups')
    ).all()

    print(users)

    for user in users:
        if user.all_groups:
            user.group_name = user.all_groups[0].name
        else:
            user.group_name = 'No Group Assigned'
    return render(request, 'admin/dashboard.html', {"users": users})



@user_passes_test(is_admin,login_url="no_permission")
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

        
@user_passes_test(is_admin,login_url="no_permission")
def create_group(request):
    form =Create_group_form()
    if request.method=="POST":
        form=Create_group_form(request.POST)
        if form.is_valid():
            group=form.save()
            messages.success(request,f"Group {group.name} create successfully")
            return redirect("create_group")
        
    return render(request,"admin/create_group.html",{"form":form})


@user_passes_test(is_admin,login_url="no_permission")
def group_list(request):
    groups=Group.objects.prefetch_related("permissions").all()
    return render(request,"admin/group_list.html",{"groups":groups})