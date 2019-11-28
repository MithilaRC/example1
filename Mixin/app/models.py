from django.db import models

# Create your models here.
class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    salary = models.FloatField()

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)

