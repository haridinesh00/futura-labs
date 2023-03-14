from django.shortcuts import render


# Create your views here.
def dashboard(requests):
    return render(requests, 'index.html')


def error_page(requests):
    return render(requests, '404.html')


def about(requests):
    return render(requests, 'about.html')


def booking(requests):
    return render(requests, 'booking.html')


def contact(requests):
    return render(requests, 'contact.html')


def service(requests):
    return render(requests, 'service.html')


def team(requests):
    return render(requests, 'team.html')


def testimonial(requests):
    return render(requests, 'testimonial.html')
