from django import forms
from django.forms import fields
from django.forms.formsets import all_valid

from testApp.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields= '__all__'