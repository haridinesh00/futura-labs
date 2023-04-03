from django.contrib import messages
from django.shortcuts import render, redirect

from app.forms import FeedbackForm
from app.models import Feedback


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
            # return redirect('login_view')
        else:
            print("Fill all required fields")
    return render(request, 'customer/feedback.html', {'feedback_form': feedback_form})


def feedback_view(request):
    u = request.user
    data = Feedback.objects.filter(user=u)
    return render(request, 'customer/feedback_view.html', {'data': data})



