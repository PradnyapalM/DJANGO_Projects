from django.contrib import admin
from django.db import models
from testApp.models import FilterDemo
# Register your models here.

class AdminFilterDemo(admin.ModelAdmin):
    list_display=['name','subject','dept','date']

admin.site.register(FilterDemo,AdminFilterDemo)