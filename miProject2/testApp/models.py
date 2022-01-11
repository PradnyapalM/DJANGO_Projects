from django.db import models

# Create your models here.

# 1. abstract model Inheritance
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    class Meta:
        abstract = True
    
    
    
        
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

  
    
   

class Teacher(ContactInfo):
    subject = models.CharField(max_length=256)
    salary = models.FloatField()


    
# 2. Multi table Inheritance
class ContactInfo1(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    def __str__(self):
        return self.name
        
class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=256)
    salary = models.FloatField()

# 3. Multilevel Inheritance

class Parent(models.Model):
    fd1 = models.CharField(max_length=50)
    fd2 = models.CharField(max_length=50)

class Child(Parent):
    fd3 = models.CharField(max_length=50)
    fd4 = models.CharField(max_length=50)

class SubChild(Child):
    fd5 = models.CharField(max_length=50)
