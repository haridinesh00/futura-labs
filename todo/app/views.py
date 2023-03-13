from django.shortcuts import render, redirect

from app.forms import TodoForm
from app.models import Todo


# Create your views here.

def welcome(requests):
    return render(requests, 'newdash/Modified_files/landing.html')


def dash(requests):
    return render(requests, 'newdash/Modified_files/index.html')


def base(requests):
    return render(requests, 'newdash/Modified_files/base.html')


# create todoapp
def addData(requests):
    form = TodoForm()
    if requests.method == "POST":
        form = TodoForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('addData')
    return render(requests, 'newdash/Modified_files/demo.html', {"form": form})


# read/view
def view(requests):
    data = Todo.objects.all()
    return render(requests, 'newdash/Modified_files/index.html', {"data": data})


def display(requests):
    data = Todo.objects.all()
    return render(requests, 'newdash/Modified_files/disp_table.html', {"data": data})


# delete function
def delete(requests, id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('display')


def update(requests, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if requests.method == 'POST':
        form = TodoForm(requests.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('display')
    return render(requests, 'newdash/Modified_files/update.html', {'form':form})
