from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def datetimeInfo(request):
    date = datetime.datetime.now()
    h=int(date.strftime("%H"))

    msg="<h1>Hello Guest very"
    if h<12:
        msg=msg+"Good Morning"
    elif h<16:
        msg=msg+"Good Afternoon"

    elif h<21:
        msg=msg+"Good Evening"

    else:
        msg=msg+"Good Night!"

    msg=msg+"</h1><hr>"
    msg=msg+"Now Server time is :"+str(date)+"</h1>"

    return HttpResponse(msg)
