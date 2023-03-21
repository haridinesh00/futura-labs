from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from app.forms import LoginRegister, WorkerForm


# Create your views here.
def landing(requests):
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


def Login(requests):
    return render(requests, 'login.html')


# ------------------------------------------------------------------


def basicTable(requests):
    return render(requests, 'dashboard/basic-table.html')


def basicElements(requests):
    return render(requests, 'dashboard/basic_elements.html')


def buttons(requests):
    return render(requests, 'dashboard/buttons.html')


def register(requests):
    return render(requests, 'dashboard/register.html')


def typography(requests):
    return render(requests, 'dashboard/typography.html')


def dashboard(requests):
    return render(requests, 'dashboard/dashboard.html')


def worker_dashboard(requests):
    return render(requests, 'dashboard/worker_dashboard.html')


def blank(requests):
    return render(requests, 'dashboard/blank-page.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('dashboard')
            elif user.is_worker:
                return redirect('worker_dashboard')
            # elif user.is_user:
            #     return redirect('user_home')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerForm()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_form = WorkerForm(request.POST)
        if user_form.is_valid() and worker_form.is_valid():
            u = user_form.save(commit=False)
            u.is_worker = True
            u.save()
            worker = worker_form.save(commit=False)
            worker.user = u
            worker.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('login_view')
    return render(request, 'dashboard/register.html', {'user_form': user_form, 'worker_form': worker_form})
