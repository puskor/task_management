from django import forms 
from tasks.models import Task

# django form
class Task_forms(forms.Form):
    title=forms.CharField(max_length=10 , label="Title")
    description=forms.CharField(widget=forms.Textarea,label="Description")
    due_date=forms.DateField(widget=forms.SelectDateWidget , label="Entry Date")
    employee=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[],label="Add employe")
    
    def __init__(self,*ergs,**kwargs):
        employees=kwargs.pop("employees" , [])
        super().__init__(*ergs,**kwargs)
        self.fields['assigned_to'].choices=[(emp.id,emp.name) for emp in employees]

# django model form

class Task_model_form(forms.ModelForm):
    class Meta:
        model=Task
        # fields='__all__'
        fields=["title","description","due_date","assigned_to"]
        
        labels={
            "assigned_to":"Assigned to"
        }
        
        widgets={
            "title":forms.TextInput(attrs={
                'class':"border-red-400 border-2 w-full rounded-lg ","placeholder":"Title"}),
            "description":forms.Textarea(attrs={
                'class':"border-red-400 border-2 w-full rounded-lg ","placeholder":"Description"}),
            "due_date":forms.SelectDateWidget(attrs={
                'class':"border-red-400 border-2 rounded-lg "}),
            "assigned_to":forms.CheckboxSelectMultiple
        }