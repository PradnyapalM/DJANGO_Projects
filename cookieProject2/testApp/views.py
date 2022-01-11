from os import name
from django.http import response
from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request,'testApp/name.html')


def age_view(request):
    # Reading data from name.html
    name=request.GET.get('name') 
    response=render(request,'testapp/age.html',{'name':name}) 
    response.set_cookie('name',name) 
    return response



def gf_view(request):
    age = request.GET.get('age')
    response=render(request,'testapp/gf.html',{'age':age})
    response.set_cookie('age',age) 
    return response


def results_view(request):
    gfname = request.GET.get('gfname')
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    response =  render(request,'testApp/result.html',{'gfname':gfname,'age':age,'name':name})
    return response