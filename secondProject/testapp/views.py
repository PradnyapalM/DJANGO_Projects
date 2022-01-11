from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def timeinfo(request):
    date=datetime.datetime.now()
    msg="<h1> Hello Friend Good Evening</h1><hr>"
    msg=msg+"<h1>Now Server Time is:"+str(date)+'</h1>'

    return HttpResponse(msg)