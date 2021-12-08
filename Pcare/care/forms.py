from django import forms
from django.forms import fields
from .models import Addservice,Servicesmodel

class TodoForm(forms.ModelForm):
    class Meta:
        model=Addservice
        fields=["id","s_name"]
