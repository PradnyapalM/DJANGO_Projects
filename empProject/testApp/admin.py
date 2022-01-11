# from DJANGOPROJECTS.empProject.testApp.models import Employee
from django.contrib import admin
from django.db.models.base import Model
from testApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']


admin.site.register(Employee,EmployeeAdmin)
 