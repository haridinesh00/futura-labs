from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Customer, Worker, Login


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ("user",)


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        exclude = ("user",)


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('__all__')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')