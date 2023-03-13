from django.urls import path

from app import views

urlpatterns = [
    path('', views.Hello, name='Hello'),
    path('Haii', views.Hai, name='Hai'),
    path('new_con', views.new_con, name='new_con'),
]
