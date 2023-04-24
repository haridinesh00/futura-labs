from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import ScheduleWork
from app.models import WorkSchedule, BookAppointment


def dash(request):
    return render(request, 'workmanager/dash.html')


def schedule_work(request):
    schedule_form = ScheduleWork()
    if request.method == 'POST':
        u = request.user
        schedule_form = ScheduleWork(request.POST)
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.user = u
            schedule.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('works')
    return render(request, 'workmanager/schedule_work.html', {'schedule_form': schedule_form})


def works(request):
    u = request.user
    data = WorkSchedule.objects.filter(user=u)
    return render(request, 'workmanager/works.html', {'data': data})


def delete_sch(requests, id):
    data = WorkSchedule.objects.get(id=id)
    data.delete()
    return redirect('works')


def update_sch(requests, id):
    work = WorkSchedule.objects.get(id=id)
    form = ScheduleWork(instance=work)
    if requests.method == 'POST':
        form = ScheduleWork(requests.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('works')
    return render(requests, 'workmanager/update.html', {'form': form})


def my_appointments(request):
    # data = BookAppointment.objects.all()
    worker = WorkSchedule.objects.filter(user=request.user)
    data = BookAppointment.objects.filter(schedule__in=worker)
    return render(request, 'workmanager/my_appointments.html', {'data': data})


def accept_app(request, id):
    data = BookAppointment.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect('my_appointments')


def reject_app(request, id):
    data = BookAppointment.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('my_appointments')
