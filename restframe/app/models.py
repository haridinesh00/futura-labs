from django.db import models


# Create your models here.
class District(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
