from os import name
from django.shortcuts import render

from . import forms
# Create your views here.

def additem_view(request):
    form= forms.AddItemForm()
    if request.method == 'POST': 
        name=request.POST['name']
        quantity= request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(0)
    return render(request,'testApp/additems.html',{'form':form})

def display_view(request):
    return render(request,'testApp/displayitems.html')

def sessioninfo_view(request):
    session=request.session
    age = session.get_expiry_age()
    date = session.get_expiry_date()
    print('Expiray age', age)
    print('Expiray Date',date)
    return render(request,'testApp/additems.html')


