from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import ScheduleWork
from app.models import WorkSchedule


def dash(request):
    return render(request, 'workmanager/dash.html')


def schedule_work(request):
    schedule_form = ScheduleWork()
    if request.method == 'POST':
        u = request.user
        schedule_form = ScheduleWork(request.POST, request.FILES)
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.user = u
            schedule.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('admin_workers')
    return render(request, 'workmanager/schedule_work.html', {'schedule_form': schedule_form})


def works(request):
    u = request.user
    data = WorkSchedule.objects.filter(user=u)
    return render(request, 'workmanager/works.html', {'data': data})
