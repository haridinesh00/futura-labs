from django.shortcuts import render


def dash(request):
    return render(request, 'workmanager/dash.html')
