from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'newsApp/index.html')

def movies(request):
    head_msg="Latest Movies info"
    msg1="Matrix 2021"
    msg2="christamas will soon"
    msg3="codewar"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}

    return render(request,'newsApp/news.html',context=my_dict)

def politics(request):
    head_msg="Latest Politics"
    msg1="end times"
    msg2="New York"
    msg3="Apple"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}

    return render(request,'newsApp/news.html',context=my_dict)

def sports(request):
    head_msg="Latest Sports info"
    msg1="Football"
    msg2="Ronaldo"
    msg3="Chess"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}

    return render(request,'newsApp/news.html',context=my_dict)