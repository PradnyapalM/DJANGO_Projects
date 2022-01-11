from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mumjobs(request):
    msg="<h1>Mumbai Jobs Information</h1>"
    return HttpResponse(msg)

def punejobs(request):
    msg="<h1>Pune Jobs Information</h1>"
    return HttpResponse(msg)

def ngpjobs(request):
    msg="<h1>Nagpur Jobs Information</h1>"
    return HttpResponse(msg)
def hydjobs(request):
    msg="<h1>Hydrabad Jobs Information</h1>"
    return HttpResponse(msg)
