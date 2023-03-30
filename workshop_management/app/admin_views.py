from django.shortcuts import render, redirect

from app.forms import WorkerForm
from app.models import Worker, Customer


def dash(request):
    return render(request, 'admin/dash.html')


def worker_dashboard(requests):
    data = Worker.objects.all()
    return render(requests, 'admin/worker_list.html', {'data': data})


def customer_dashboard(request):
    data = Customer.objects.all()
    return render(request, 'admin/customer_list.html', {'data': data})


def delete(requests, id):
    data = Worker.objects.get(id=id)
    data.delete()
    return redirect('admin_workers')


def delete_cus(requests, id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('admin_customers')


def update(requests, id):
    work = Worker.objects.get(id=id)
    form = WorkerForm(instance=work)
    if requests.method == 'POST':
        form = WorkerForm(requests.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('admin_workers')
    return render(requests, 'admin/update.html', {'form': form})
