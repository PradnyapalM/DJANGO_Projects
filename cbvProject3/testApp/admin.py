from django.contrib import admin
from testApp.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
     list_dispaly = ['name','location','ceo']
     
admin.site.register(Company,CompanyAdmin)