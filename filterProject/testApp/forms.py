from django import forms
from django.forms import fields
from testApp.models import FilterDemo

class FilterForm(forms.ModelForm):
    class Meta:
        model=FilterDemo
        fields='__all__'