from django import forms
from django.forms.fields import IntegerField

class NameForm(forms.Form):
    name = forms.CharField()

class AgeForm(forms.Form):
    age = forms.IntegerField()

class gfForm(forms.Form):
    gf = forms.CharField()