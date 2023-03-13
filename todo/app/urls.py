from django.urls import path

from app import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('dash/', views.dash, name="dash"),
    path('addData', views.addData, name="addData"),
    path('view', views.view, name="view"),
    path('display', views.display, name="display"),
    path('base', views.base, name="base"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
]
