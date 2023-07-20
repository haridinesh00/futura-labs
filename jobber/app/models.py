from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_seeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    name = models.CharField(max_length=42, null=True)
    phone = models.CharField(max_length=15, null=True)
    profile_pic = models.FileField(upload_to='documents/', null=True)
    status = models.IntegerField(default=0, null=True)
    gender = models.CharField(max_length=10)
    location = models.TextField(max_length=150)


class Job(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    expiry_date = models.DateField(null=True, blank=True)
    salary_type = models.CharField(max_length=10, default="Yearly")
    salary_min = models.CharField(max_length=10)
    salary_max = models.CharField(max_length=10)
    location = models.TextField(max_length=150)
    experience = models.IntegerField(default=0)
    qualification = models.CharField(max_length=50)
    industry = models.CharField(max_length=25)
    career_level = models.CharField(max_length=25)
