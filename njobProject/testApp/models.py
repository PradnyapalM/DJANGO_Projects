from django.db import models

# Create your models here.

class ngpjob (models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class goajob (models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()


class punejob (models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()

