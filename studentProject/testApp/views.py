from django.shortcuts import render
from testApp import forms
# Create your views here.

def student_view(request):
    form = forms.StudentForm()
    if request.method=='POST':
           form = forms.StudentForm(request.POST)

           if form.is_valid():
               form.save(commit=True)
    print("Form Data inserted Sucessfully")
    return render(request,'testApp/register.html',{'form':form})