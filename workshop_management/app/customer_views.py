from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import FeedbackForm
from app.models import Feedback, WorkSchedule, BookAppointment, Login


def dash(request):
    return render(request, 'customer/dash.html')


def feedback_register(request):
    feedback_form = FeedbackForm()
    if request.method == 'POST':
        u = request.user
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feed = feedback_form.save(commit=False)
            feed.user = u
            feed.save()
            messages.info(request, 'Feedback Submitted')
            return redirect('feedback_view')
        else:
            print("Fill all required fields")
    return render(request, 'customer/feedback.html', {'feedback_form': feedback_form})


def feedback_view(request):
    u = request.user
    data = Feedback.objects.filter(user=u)
    return render(request, 'customer/feedback_view.html', {'data': data})


def book_app(request):
    data = WorkSchedule.objects.all()
    # new_data = BookAppointment.objects.all()
    return render(request, 'customer/book.html', {'data': data})


def book_history(request):
    # data = BookAppointment.objects.all()
    worker = Login.objects.get(username=request.user)
    data = BookAppointment.objects.filter(worker=worker)
    return render(request, 'customer/booking_history.html', {'data': data})


def book(request, id):
    schedule = WorkSchedule.objects.get(id=id)
    if request.method == 'POST':
        schedule.customer = str(request.user)
        schedule.save()
        messages.info(request, 'Appointment Booked')
        return redirect('book_app')


def confirm_app(request):
    schedule = WorkSchedule.objects.all()
    return render(request, 'customer/take_app.html', {'schedule': schedule})


def appointment(request, id):
    # form = AppointmentForm()
    schedule = WorkSchedule.objects.get(id=id)
    worker = Login.objects.get(username=request.user)
    appoint = BookAppointment.objects.filter(worker=worker, schedule=schedule)
    if appoint.exists():
        messages.info(request, 'Already requested ')
        return redirect('book_app')
    else:
        if request.method == 'POST':
            obj = BookAppointment()
            obj.worker = worker
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked')
            return redirect('book_history')
    return render(request, 'customer/take_app.html', {'schedule': schedule})
