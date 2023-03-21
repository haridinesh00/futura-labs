from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=150)


class Worker(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=150)
