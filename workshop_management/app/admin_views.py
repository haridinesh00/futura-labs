from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control

from app.forms import WorkerForm, WorkerCategoryForm, BillGenerate
from app.models import Login, Feedback, WorkerCategory, WorkSchedule, BookAppointment, Bill


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def dash(request):
    return render(request, 'admin/dash.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def worker_register(request):
    worker_form = WorkerForm()
    # data = WorkerCategory.objects.all()
    if request.method == 'POST':
        worker_form = WorkerForm(request.POST, request.FILES)
        if worker_form.is_valid():
            user = worker_form.save(commit=False)
            user.is_worker = True
            user.save()
            messages.success(request, 'Worker Registration Successful')
            return redirect('admin_workers')
    return render(request, 'admin/worker_register.html', {'worker_form': worker_form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def worker_dashboard(requests):
    data = Login.objects.all()
    return render(requests, 'admin/worker_list.html', {'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def worker_schedules(requests):
    data = WorkSchedule.objects.all()
    return render(requests, 'admin/worker_schedules.html', {'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_dashboard(request):
    data = Login.objects.all()
    return render(request, 'admin/customer_list.html', {'data': data})


#
# def new_request(request):
#     data = Worker.objects.all()
#     return render(request, 'admin/new_request.html', {'data': data})
#
#
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def delete(requests, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('admin_workers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def delete_cus(requests, id):
    data = Login.objects.get(id=id)
    data.delete()
    return redirect('admin_customers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def update(requests, id):
    work = Login.objects.get(id=id)
    form = WorkerForm(instance=work)
    if requests.method == 'POST':
        form = WorkerForm(requests.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('admin_workers')
    return render(requests, 'admin/update.html', {'form': form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def feedbacks(request):
    u = request.user
    data = Feedback.objects.all()
    return render(request, 'admin/feedbacks.html', {'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def reply_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.success(request, 'Reply send')
        return redirect('feedbacks')
    return render(request, 'admin/reply_feedback.html', {'feedback': feedback})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def category_register(request):
    category_form = WorkerCategoryForm()
    data = WorkerCategory.objects.all()
    if request.method == 'POST':
        category_form = WorkerCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_register')
    return render(request, 'admin/categories.html', {'category': category_form, 'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def accept(request, id):
    data = Login.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect('admin_workers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def reject(request, id):
    data = Login.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('admin_workers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def all_appointments(request):
    data = BookAppointment.objects.all()
    return render(request, 'admin/all_appointments.html', {'data': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def generate_bill(request, id):
    bill_form = BillGenerate()
    appoint = BookAppointment.objects.get(id=id)
    check = Bill.objects.filter(appoint=appoint)
    if check.exists():
        messages.info(request, 'Already exists ')
        return redirect('all_appointments')
    else:
        if request.method == 'POST':
            bill_form = BillGenerate(request.POST)
            if bill_form.is_valid():
                user = bill_form.save(commit=False)
                user.appoint = appoint
                print(appoint)
                user.save()
                return redirect('all_appointments')
    return render(request, 'admin/generate_bill.html', {'bill_form': bill_form})
