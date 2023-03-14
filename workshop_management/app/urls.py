from django.urls import path

from app import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('404', views.error_page, name="error_page"),
    path('about', views.about, name="about"),
    path('booking', views.booking, name="booking"),
    path('contact', views.contact, name="contact"),
    path('service', views.service, name="service"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
]
