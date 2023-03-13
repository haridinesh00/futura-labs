from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(requests):
    return HttpResponse('Hello World')

def hello(requests):
    return render(requests, 'index.html')

def dashboard(requests):
    return render(requests, 'dash/dashboard.html')
