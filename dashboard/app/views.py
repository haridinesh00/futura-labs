from django.shortcuts import render


# Create your views here.
def welcome(requests):
    return render(requests, 'newdash/Modified_files/index.html')

def error(requests):
    return render(requests, 'newdash/Modified_files/404.html')

def blank(requests):
    return render(requests, 'newdash/Modified_files/blank.html')

def button(requests):
    return render(requests, 'newdash/Modified_files/button.html')

def chart(requests):
    return render(requests, 'newdash/Modified_files/chart.html')

def element(requests):
    return render(requests, 'newdash/Modified_files/element.html')

def form(requests):
    return render(requests, 'newdash/Modified_files/form.html')

def signin(requests):
    return render(requests, 'newdash/Modified_files/signin.html')

def signup(requests):
    return render(requests, 'newdash/Modified_files/signup.html')

def table(requests):
    return render(requests, 'newdash/Modified_files/table.html')

def typography(requests):
    return render(requests, 'newdash/Modified_files/typography.html')

def widget(requests):
    return render(requests, 'newdash/Modified_files/widget.html')
