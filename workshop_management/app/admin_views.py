from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import WorkerForm, WorkerCategoryForm
from app.models import Login, Feedback, WorkerCategory, WorkSchedule


def dash(request):
    return render(request, 'admin/dash.html')


def worker_register(request):
    worker_form = WorkerForm()
    # data = WorkerCategory.objects.all()
    if request.method == 'POST':
        worker_form = WorkerForm(request.POST, request.FILES)
        if worker_form.is_valid():
            user = worker_form.save(commit=False)
            user.is_worker = True
            user.save()
            messages.info(request, 'Worker Registration Successful')
            return redirect('admin_workers')
    return render(request, 'dashboard/register.html', {'worker_form': worker_form})


def worker_dashboard(requests):
    data = Login.objects.all()
    return render(requests, 'admin/worker_list.html', {'data': data})


def worker_schedules(requests):
    data = WorkSchedule.objects.all()
    return render(requests, 'admin/worker_schedules.html', {'data': data})


def customer_dashboard(request):
    data = Login.objects.all()
    return render(request, 'admin/customer_list.html', {'data': data})


#
# def new_request(request):
#     data = Worker.objects.all()
#     return render(request, 'admin/new_request.html', {'data': data})
#
#
def delete(requests, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('admin_workers')


def delete_cus(requests, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('admin_customers')


def update(requests, id):
    work = Login.objects.get(id=id)
    form = WorkerForm(instance=work)
    if requests.method == 'POST':
        form = WorkerForm(requests.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('admin_workers')
    return render(requests, 'admin/update.html', {'form': form})


def feedbacks(request):
    u = request.user
    data = Feedback.objects.all()
    return render(request, 'admin/feedbacks.html', {'data': data})


def reply_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send')
        return redirect('feedbacks')
    return render(request, 'admin/reply_feedback.html', {'feedback': feedback})


def category_register(request):
    category_form = WorkerCategoryForm()
    data = WorkerCategory.objects.all()
    if request.method == 'POST':
        category_form = WorkerCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_register')
    return render(request, 'admin/categories.html', {'category': category_form, 'data': data})


def accept(request, id):
    data = Login.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect('admin_workers')


def reject(request, id):
    data = Login.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('admin_workers')
