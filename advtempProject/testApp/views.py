from django.shortcuts import render

# Create your views here.

def home_view(request):
     return render(request,'testApp/home.html')


def movie_view(request):
     return render(request,'testApp/movie.html')

def politics_view(request):
     return render(request,'testApp/politics.html')

def sports_view(request):
     return render(request,'testApp/sports.html')