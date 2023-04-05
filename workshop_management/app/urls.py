from django.urls import path

from app import views, admin_views, customer_views, workmanager_views

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
    path('customer_register', views.customer_register, name="customer_register"),
    path('customer_dashboard', views.customer_dashboard, name="customer_dashboard"),
    path('logout_view', views.logout_view, name="logout_view"),


    #admin

    path('admin_dash', admin_views.dash, name="admin_dash"),
    path('admin_workers', admin_views.worker_dashboard, name="admin_workers"),
    path('admin_customers', admin_views.customer_dashboard, name="admin_customers"),
    path('delete/<int:id>/', admin_views.delete, name="delete"),
    path('delete_cus/<int:id>/', admin_views.delete_cus, name="delete_cus"),
    path('update/<int:id>/', admin_views.update, name="update"),
    path('feedbacks', admin_views.feedbacks, name="feedbacks"),
    path('reply_feedback/<int:id>/', admin_views.reply_feedback, name="reply_feedback"),

    #customer

    path('customer_dash', customer_views.dash, name="customer_dash"),
    path('feedback_register', customer_views.feedback_register, name="feedback_register"),
    path('feedback_view', customer_views.feedback_view, name="feedback_view"),


    #work manager

    path('workmanager_dash', workmanager_views.dash, name="workmanager_dash"),
]

