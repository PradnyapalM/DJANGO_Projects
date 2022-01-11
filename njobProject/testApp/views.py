from django.shortcuts import render
from testApp.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def index1(request):
    return render(request,'testApp/index.html')

def ngpjobs1(request):
    jobs_list = ngpjob.objects.order_by('date')

    # post_list = Post.objects.all()
    paginator = Paginator(jobs_list,8)
    page_number = request.GET.get('page')
    try:
        jobs_list = paginator.page(page_number)
    except PageNotAnInteger:
        jobs_list = paginator.page(1)
    except EmptyPage:
        jobs_list = paginator.page(paginator.num_pages)
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/ngpjob.html',context=my_dict)

def pune1(request):
    return render(request,'testApp/punejob.html')

def goa1(request):
    return render(request,'testApp/goajob.html')