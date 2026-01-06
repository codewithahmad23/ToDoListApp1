from django import  forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter task title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter description', 'rows':3}),
            'completed': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
