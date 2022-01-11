from django.shortcuts import render
import datetime
# Create your views here.
def hi(request):
    date=datetime.datetime.now()
    name=" Tips!!!  "
    msg=""
    h=int(date.strftime('%H'))
    if h<12:
        msg="Good Morning!!"
    if h<16:
        msg="Good Afternoon!!"
    if h<22:
        msg="Good Evening!!"
    else:
        msg="Good Night"



    my_dict={"date":date,"guest":name,"msg":msg}
    return render(request,"testApp/nur.html",context=my_dict)