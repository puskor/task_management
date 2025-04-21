from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group,Permission
from django import forms
import re
from tasks.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm



class RegisterForm(StyledFormMixin,UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        
        for field_name in ['username','password1','password2']:
            self.fields[field_name].help_text = None
            
class CustomRegisterForm(StyledFormMixin,forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        errors = []

        if len(password) < 8:
            errors.append('Password must be at least 8 character long')

        if not re.search(r'[A-Z]', password):
            errors.append(
                'Password must include at least one uppercase letter.')

        if not re.search(r'[a-z]', password):
            errors.append(
                'Password must include at least one lowercase letter.')

        if not re.search(r'[0-9]', password):
            errors.append('Password must include at least one number.')

        if not re.search(r'[@#$%^&+=]', password):
            errors.append(
                'Password must include at least one special character.')

        if errors:
            raise forms.ValidationError(errors)
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    

class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        
        
        
class AssignRoleForm(StyledFormMixin,forms.Form):
    role=forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a role"
    )
    
    
# class Create_group_form(StyledFormMixin,forms.ModelForm):
#     permissions=forms.ModelMultipleChoiceField(
#         queryset=Permission.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False,
#         label="Assign permission"
#     )
    
#     class Meta:
#         model= Group
#         fields=["name","permissions"]

class Create_group_form(StyledFormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Assign permission"
    )

    class Meta:
        model = Group
        fields = ["name", "permissions"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['permissions'].queryset = Permission.objects.select_related('content_type')
