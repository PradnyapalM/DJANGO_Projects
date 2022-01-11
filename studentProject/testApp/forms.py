from django import forms
from django.db.models.base import Model
from django.forms import fields, models
from testApp.models import Student

class StudentForm(forms.ModelForm):
     class Meta:
         model=Student
         fields='__all__'
        
    
