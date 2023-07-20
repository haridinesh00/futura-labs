from django.contrib.auth.forms import UserCreationForm
from django import forms

from app.models import Login, Job


class DateInput(forms.DateInput):
    input_type = 'date'


class SeekerForm(UserCreationForm):
    # email = forms.CharField(validators=[
    #     RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$', message='Please enter a valid Email')])
    # phone = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Login
        fields = ("name", "email", "phone", "location", "username", "password1", "password2")


class EmployerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ("name", "email", "phone", "location", "profile_pic", "username", "password1", "password2")


class JobForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Job
        fields = ("title", "description", "expiry_date", "salary_type", "salary_min", "salary_max", "location")
