from django.contrib.auth.models import AbstractUser
from django.db import models


class WorkerCategory(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    name = models.CharField(max_length=42, null=True)
    phone = models.CharField(max_length=15, null=True)
    profile_pic = models.FileField(upload_to='documents/', null=True)
    status = models.IntegerField(default=0, null=True)
    category = models.ForeignKey(WorkerCategory, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=150)


class WorkSchedule(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    customer = models.CharField(max_length=20, null=True, blank=True)

# class Customer(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE)
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     phone = models.CharField(max_length=15)
#     profile_pic = models.FileField(upload_to='documents/')


# class Worker(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name="worker")
#     category = models.ForeignKey(WorkerCategory, on_delete=models.CASCADE)
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     phone = models.CharField(max_length=15)
#     dob = models.DateField()
#     gender = models.CharField(max_length=10)
#     address = models.TextField(max_length=150)
#     profile_pic = models.FileField(upload_to='documents/')
#     status = models.IntegerField(default=0)


class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=150)
    reply = models.CharField(max_length=150, null=True, blank=True)


class BookAppointment(models.Model):
    schedule = models.ForeignKey(WorkSchedule, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0, null=True)


class Bill(models.Model):
    work_done = models.CharField(max_length=100)
    bill = models.FloatField(max_length=10)
    date = models.DateField(null=True, blank=True)
    appoint = models.ForeignKey(BookAppointment, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.IntegerField(default=0, null=True)


class Payment(models.Model):
    card_num = models.IntegerField(max_length=16)
    expiry_date = models.DateField(null=True, blank=True)
    cvv = models.IntegerField(max_length=3)
