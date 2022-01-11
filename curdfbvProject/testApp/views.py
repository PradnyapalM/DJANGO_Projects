from django.shortcuts import redirect, render
#from DJANGOPROJECTS.curdfbvProject.testApp.forms import EmployeeForm
from testApp import forms
from testApp.models import Employee
# Create your views here.


def retrieve_view(request):
    employees = Employee.objects.all()
    return render(request,'testApp/index.html',{'employees':employees})

def create_view(request):
    form = forms.EmployeeForm()
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('/home/')
    return render(request,'testApp/create.html',{'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/home/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request,'testApp/update.html',{'employee':employee})