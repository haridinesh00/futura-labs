from django.db import models


# Create your models here.

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     grade = models.CharField(max_length=3)
#     phone_number = models.IntegerField()
#     dob = models.DateField()

class Todo(models.Model):
    event = models.CharField(max_length=30)
    date = models.DateField()
