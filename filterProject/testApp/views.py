from django.shortcuts import render
from testApp.models import FilterDemo
# Create your views here.

def upper_view(request):
    data_list=FilterDemo.objects.all()
    return render(request,'testApp/upper.html',{'data_list':data_list})


def lower_view(request):
    data_list=FilterDemo.objects.all()
    return render(request,'testApp/lower.html',{'data_list':data_list})