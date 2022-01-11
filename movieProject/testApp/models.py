from django.db import models

# Create your models here.

class Movie(models.Model):
    rdate = models.DateField()
    moviename = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
    heroin = models.CharField(max_length=50)
    rating = models.IntegerField()
