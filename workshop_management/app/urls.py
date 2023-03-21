from django.urls import path

from app import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('404', views.error_page, name="error_page"),
    path('about', views.about, name="about"),
    path('booking', views.booking, name="booking"),
    path('contact', views.contact, name="contact"),
    path('service', views.service, name="service"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
    path('Login', views.Login, name="Login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('basictable', views.basicTable, name="basicTable"),
    path('basicelements', views.basicElements, name="basicElements"),
    path('buttons', views.buttons, name="buttons"),
    path('register', views.register, name="register"),
    path('typography', views.typography, name="typography"),
    path('blank', views.blank, name="blank"),
    path('login_view', views.login_view, name="login_view"),
    path('worker_register', views.worker_register, name="worker_register"),
    path('worker_dashboard', views.worker_dashboard, name="worker_dashboard"),
]
