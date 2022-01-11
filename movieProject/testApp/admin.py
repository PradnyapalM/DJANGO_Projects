from django.contrib import admin

from testApp.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    list_display=['rdate','moviename','hero','heroin','rating']

admin.site.register(Movie,MovieAdmin)
