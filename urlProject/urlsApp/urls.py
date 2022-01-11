from django.conf.urls import url
from urlsApp import views

urlpatterns = [
    
    url('Mumbai/',views.mumjobs),
    url('Nagpur/',views.ngpjobs),
    url('Pune/',views.punejobs),
    url('Hydrabad/',views.hydjobs),


]
