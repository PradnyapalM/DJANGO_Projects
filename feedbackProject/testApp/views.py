from django.shortcuts import render
from django.utils.html import format_html
from . import forms

# Create your views here.

def thankyou_view(request):
    return render(request, 'testApp/thankyou.html')#{'name':form.cleaned_data['name']}#)

def feedback_view(request):
    if request.method == 'GET':
        form =forms.FeedBackForm()
        return render(request,'testApp/feedback.html',{'form':form})

    if request.method == 'POST':
        form =forms.FeedBackForm(request.POST)

        if form.is_valid():
            print('Form validation sucess and Printing Feedback is Info')
            print('Student Name', form.cleaned_data['name'])
            print('Student Roll No', form.cleaned_data['rollno'])
            print('Student Mail', form.cleaned_data['email'])
            print('Student Feedback', form.cleaned_data['feedback'])
            return thankyou_view(request)

    return render(request,'testApp/feedback.html',{'form':form})
            

     
        
       