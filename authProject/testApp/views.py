from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  . import forms
from django.http import HttpResponseRedirect

# Create your views here.

def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def javaexams_view(request):
    return render(request,'testApp/javaexams.html')

@login_required
def pythonexams_view(request):
    return render(request,'testApp/pythonexams.html')

@login_required
def apptitudeexams_view(request):
    return render(request,'testApp/apptitudeexams.html')


def logout_view(request):
    return render(request,'testApp/logout.html')


def signup_view(request):
    form = forms.SignUpForm()
    if request.method=='POST':
        form= forms.SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()        
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})