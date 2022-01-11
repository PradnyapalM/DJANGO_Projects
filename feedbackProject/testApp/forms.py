from django import forms
from django.core import validators
from django.forms.widgets import HiddenInput

def starts_with_d(value):
    if value[0].lower()!= 'd':
        raise forms.ValidationError("Name should be start with d | D")

class FeedBackForm(forms.Form):
    name = forms.CharField() #validators=[starts_with_d]
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)

    feedback= forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False,widget=HiddenInput)
    # def clean_name(self):
    #     inputname= self.cleaned_data['name']
    #     if len(inputname)<4:
    #      raise forms.ValidationError("The length of name Filed should >=4")
    #     return inputname 
     
    # def clean_rollno(self):
    #     inputname = self.cleaned_data["rollno"]
    #     print('validating roll no')
    #     return inputname
        
    # def clean_email(self):
    #     inputname = self.cleaned_data["email"]
    #     print('validating email address')
    #     return inputname

    # def clean_feedback(self):
    #     inputname = self.cleaned_data["feedback"]
    #     print('validating feedback')
    #     return inputname
    

    def clean(self):
        print("Total form validation")
        clean_data = super().clean()
        inputname = clean_data['name']
        if len(inputname)<5:
            raise forms.ValidationError("Name should min 5 characters")
        inputrollno = clean_data['rollno']
        if len(str (inputrollno))!=3:
            raise forms.ValidationError("Minimum 3 digit contains")

        inputpwd = clean_data['password']
        inputrpwd = clean_data['rpassword']

        if inputpwd != inputrpwd:
            raise forms.ValidationError("Password Not matched")
        
        print("BOT Validation")
        bot_handler_value= clean_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError("Thanks *BOT* request Denined")





        
        
        
    
    
     
