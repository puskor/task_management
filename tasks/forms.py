from django import forms 
from tasks.models import Task,Task_details

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


class StyledFormMixin:
    """ Mixing to apply style to form field"""

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 m-4 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })
                
class Task_model_form(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status','due_date', 'assigned_to']
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }

    """ Widget using mixins """

    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styled_widgets()

# class Task_model_form(forms.ModelForm):
#     class Meta:
#         model=Task
#         # fields='__all__'
#         fields=["title","description","due_date","assigned_to"]
        
#         labels={
#             "assigned_to":"Assigned to"
#         }
        
#         widgets={
#             "title":forms.TextInput(attrs={
#                 'class':"border-red-400 border-2 w-full rounded-lg ","placeholder":"Title"}),
#             "description":forms.Textarea(attrs={
#                 'class':"border-red-400 border-2 w-full rounded-lg ","placeholder":"Description"}),
#             "due_date":forms.SelectDateWidget(attrs={
#                 'class':"border-red-400 border-2 rounded-lg "}),
#             "assigned_to":forms.CheckboxSelectMultiple
#         }
        
class TaskDetailModelForm(StyledFormMixin,forms.ModelForm):
    
    class Meta:
        model = Task_details
        fields = ["priority","nodes"]
        
    def __init__(self, *arg, **kwarg):
            super().__init__(*arg, **kwarg)
            self.apply_styled_widgets()
    

