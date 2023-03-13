from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Hello(requests):
    return HttpResponse('Hello')

def Hai(requests):
    return render(requests, 'hello.html')

def new_con(requests):
    return render(requests, "index.html")
