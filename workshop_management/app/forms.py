import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from app.models import Login, Feedback, WorkSchedule, BookAppointment, Bill, Payment
from django.core import validators

from app.models import WorkerCategory
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not a valid number')


class CustomerForm(UserCreationForm):
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a valid Email')])
    phone = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Login
        fields = ("name", "email", "phone", "profile_pic", "username", "password1", "password2")


class WorkerCategoryForm(forms.ModelForm):
    # description = forms.CharField(max_length=25)

    class Meta:
        model = WorkerCategory
        fields = ("title", "description",)


class WorkerForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a valid Email')])
    phone = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Login
        fields = (
            "category", "name", "email", "phone", "gender", "address", "profile_pic", "username", "password1",
            "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Login.objects.filter(email=email).exists():
            raise ValidationError(_('This email id is already in use.'))
        return email

    def clean_mobile(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit() or len(phone) != 10:
            raise ValidationError(_('Please enter a valid 10 digit mobile number.'))
        return phone


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
    expiry_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Payment
        fields = ('card_num', 'expiry_date', 'cvv',)
