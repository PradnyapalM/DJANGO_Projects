"""cbvfinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testApp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.BeerListView.as_view(),name='beer'),
    url(r'^home/(?P<pk>\d+)/$',views.BeerDetailView.as_view(),name='detail'),
    path('create/',views.BeerCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$',views.BeerUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$',views.BeerDeleteView.as_view()),



]
