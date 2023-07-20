from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from app.forms import SeekerForm, EmployerForm, JobForm
from app.models import Login, Job


# Create your views here.
def home(request):
    return render(request, 'index.html')


def job_details(request, id):
    data = Job.objects.get(id=id)
    return render(request, 'job_details.html', {'data': data})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_seeker:
                return redirect('seeker_dashboard')
            elif user.is_employer:
                return redirect('employer_post_new_job')
            elif user.is_staff:
                return redirect('admin_dash')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def seeker_register(request):
    seeker_form = SeekerForm()
    if request.method == 'POST':
        seeker_form = SeekerForm(request.POST)
        if seeker_form.is_valid():
            user = seeker_form.save(commit=False)
            user.is_seeker = True
            user.save()
            messages.info(request, 'Customer Registration Successful')
            return redirect('login_view')
    return render(request, 'register.html')


def employer_register(request):
    employer_form = EmployerForm()
    if request.method == 'POST':
        employer_form = EmployerForm(request.POST, request.FILES)
        if employer_form.is_valid():
            user = employer_form.save(commit=False)
            user.is_employer = True
            user.save()
            messages.info(request, 'Employee Registration Successful')
            return redirect('login_view')
    return render(request, 'register_employer.html')


def seeker_dashboard(request):
    data = Login.objects.get(username=request.user)
    return render(request, 'seeker_dashboard.html', {'data': data})


def my_profile(request):
    data = Login.objects.get(username=request.user)
    return render(request, 'seeker_my_profile.html', {'data': data})


def job_listing(request):
    data = Job.objects.all()
    return render(request, 'job-listing.html', {'data': data})


def employer_post_new_job(request):
    data = Login.objects.get(username=request.user)
    job_form = JobForm()
    if request.method == 'POST':
        u = request.user
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job = job_form.save(commit=False)
            job.user = u
            job.save()
            messages.info(request, 'Job Posted Successful')
            return redirect('employer_post_new_job')
        else:
            print(job_form.errors)
    return render(request, 'employer_dash_new_job.html', {'data': data})
