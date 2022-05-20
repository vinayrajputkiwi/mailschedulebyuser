from django import forms
from .models import Task

class TaskSchedul(forms.ModelForm):
    class Meta:
        model= Task
        fields= ['task_name','user']

