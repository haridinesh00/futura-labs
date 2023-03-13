from django.urls import path

from app import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('hello', views.hello, name='hello'),
    path('dash', views.dashboard, name='dash'),
]
