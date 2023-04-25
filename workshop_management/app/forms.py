from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Login, Feedback, WorkSchedule, BookAppointment, Bill, Payment

from app.models import WorkerCategory
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ("name", "email", "phone", "profile_pic", "username", "password1", "password2")


class WorkerCategoryForm(forms.ModelForm):
    # description = forms.CharField(max_length=25)

    class Meta:
        model = WorkerCategory
        fields = ("title", "description",)


class WorkerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = (
            "category", "name", "email", "phone", "gender", "address", "profile_pic", "username", "password1",
            "password2")


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ("is_worker", "is_customer",)


# class LoginRegister(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
#
#     class Meta:
#         model = Login
#         fields = ('username', 'password1', 'password2')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)


class ScheduleWork(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = WorkSchedule
        fields = ('date', 'start_time', 'end_time',)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('schedule',)


class BillGenerate(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('work_done', 'bill', 'date',)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('card_num', 'expiry_date', 'cvv',)
