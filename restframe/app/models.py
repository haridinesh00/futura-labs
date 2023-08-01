import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class District(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    pub_date = models.DateTimeField("date published", blank=True, null=True, auto_now=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
