from django.urls import path

from app import views

urlpatterns = [
    path('district_add/', views.district_add, name="district_add"),
    path('getdata', views.getdata, name="getdata"),
    path('district_update/<int:id>', views.district_update, name="district_update"),
    ]
