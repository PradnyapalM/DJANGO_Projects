from django.contrib import admin
from testApp.models import ngpjob,punejob,goajob
# Register your models here.

class ngpjobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


class goajobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(ngpjob,ngpjobAdmin)
admin.site.register(goajob,goajobAdmin)
admin.site.register(punejob,punejobAdmin)