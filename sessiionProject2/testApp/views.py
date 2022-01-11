from django.shortcuts import render


from . import forms 
# Create your views here.

def name_view(request):
    form = forms.NameForm()
    return render(request,'testApp/name.html',{'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name']=name
    form= forms.AgeForm()
    return render(request,'testApp/age.html',{'form':form})

def gf_view(request):
    age = request.GET['age']
    request.session['age']=age
    form= forms.gfForm()
    return render(request,'testApp/gf.html',{'form':form})
def result_view(request):
    gf = request.GET['gf'] 
    request.session['gf']=gf
    return render(request,'testApp/result.html')