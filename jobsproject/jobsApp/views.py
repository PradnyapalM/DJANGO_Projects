from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hydjobs(request):
    s="<h1>Hydrabad Jobs information</h1>"
    return HttpResponse(s)

def punejobs(request):
    s="<h1>Pune Jobs information</h1>"
    return HttpResponse(s)

def mumjobs(request):
    s="<h1>Mumbai Jobs information</h1>"
    return HttpResponse(s)

def chenjobs(request):
    s="<h1>Chennai Jobs information</h1>"
    return HttpResponse(s)