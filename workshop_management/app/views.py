from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from app.forms import WorkerForm, WorkerCategoryForm, CustomerForm
from app.models import Login


def landing(requests):
    return render(requests, 'index.html')


def error_page(requests):
    return render(requests, '404.html')


def basic_elements(request):
    return render(request, 'dashboard/basic_elements.html')


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


#
#
# def Login(requests):
#     return render(requests, 'login.html')
#
#
# # ------------------------------------------------------------------
#
#
# def basicTable(requests):
#     return render(requests, 'dashboard/basic-table.html')
#
#
# def basicElements(requests):
#     return render(requests, 'dashboard/basic_elements.html')
#
#
# def buttons(requests):
#     return render(requests, 'dashboard/buttons.html')
#
#
# def register(requests):
#     return render(requests, 'dashboard/register.html')
#
#
# def typography(requests):
#     return render(requests, 'dashboard/typography.html')
#
#
# def dashboard(requests):
#     return render(requests, 'dashboard/dashboard.html')
#
#
def worker_dashboard(requests):
    data = Login.objects.all()
    return render(requests, 'dashboard/worker_dashboard.html', {'data': data})


# def customer_dashboard(request):
#     data = Customer.objects.all()
#     return render(request, 'dashboard/customer_dashboard.html', {'data': data})
#
#
# def blank(requests):
#     return render(requests, 'dashboard/blank-page.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_customer:
                return redirect('customer_dash')
            elif user.is_worker:
                return redirect('workmanager_dash')
            elif user.is_staff:
                return redirect('admin_dash')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def customer_register(request):
    customer_form = CustomerForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, request.FILES)
        if customer_form.is_valid():
            user = customer_form.save(commit=False)
            user.is_customer = True
            user.save()
            messages.info(request, 'Customer Registration Successful')
            return redirect('login_view')
    return render(request, 'dashboard/customer_register.html', {'customer_form': customer_form})


def logout_view(request):
    logout(request)
    return redirect('login_view')
