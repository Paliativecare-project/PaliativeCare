from django import forms
from django.forms import fields
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class TodoForm(forms.ModelForm):
    class Meta:
        model=Addservice
        fields=["id","s_name"]

class AddServiceForm(ModelForm):
    class Meta:
        model=UserService
        fields=['service']
