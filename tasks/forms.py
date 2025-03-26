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
        self.fields['employee'].choices=[(emp.id,emp.name) for emp in employees]

