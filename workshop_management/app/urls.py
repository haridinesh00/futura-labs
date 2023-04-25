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
    # path('Login', views.Login, name="Login"),
    # path('dashboard', views.dashboard, name="dashboard"),
    # path('basictable', views.basicTable, name="basicTable"),
    # path('basicelements', views.basicElements, name="basicElements"),
    # path('buttons', views.buttons, name="buttons"),
    # path('register', views.register, name="register"),
    # path('typography', views.typography, name="typography"),
    # path('blank', views.blank, name="blank"),
    path('login_view', views.login_view, name="login_view"),
    path('worker_dashboard', views.worker_dashboard, name="worker_dashboard"),
    path('customer_register', views.customer_register, name="customer_register"),
    # path('customer_dashboard', views.customer_dashboard, name="customer_dashboard"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('basic_elements', views.basic_elements, name="basic_elements"),


    #admin

    path('admin_dash', admin_views.dash, name="admin_dash"),
    path('admin_workers', admin_views.worker_dashboard, name="admin_workers"),
    path('admin_customers', admin_views.customer_dashboard, name="admin_customers"),
    path('delete/<int:id>/', admin_views.delete, name="delete"),
    path('delete_cus/<int:id>/', admin_views.delete_cus, name="delete_cus"),
    path('update/<int:id>/', admin_views.update, name="update"),
    path('feedbacks', admin_views.feedbacks, name="feedbacks"),
    path('reply_feedback/<int:id>/', admin_views.reply_feedback, name="reply_feedback"),
    path('category_register', admin_views.category_register, name="category_register"),
    path('worker_register', admin_views.worker_register, name="worker_register"),
    path('worker_schedules', admin_views.worker_schedules, name="worker_schedules"),
    path('all_appointments', admin_views.all_appointments, name="all_appointments"),
    path('generate_bill/<int:id>/', admin_views.generate_bill, name="generate_bill"),
    # path('accept/<int:id>/', admin_views.accept, name="accept"),
    # path('reject/<int:id>/', admin_views.reject, name="reject"),
    # path('new_request', admin_views.new_request, name="new_request"),

    #customer

    path('customer_dash', customer_views.dash, name="customer_dash"),
    path('feedback_register', customer_views.feedback_register, name="feedback_register"),
    path('feedback_view', customer_views.feedback_view, name="feedback_view"),
    path('book_app', customer_views.book_app, name="book_app"),
    path('book/<int:id>/', customer_views.book, name="book"),
    path('appointment/<int:id>/', customer_views.appointment, name="appointment"),
    path('pay_bill/<int:id>/', customer_views.pay_bill, name="pay_bill"),
    path('book_history', customer_views.book_history, name="book_history"),
    path('confirm_app', customer_views.confirm_app, name="confirm_app"),
    path('my_bills', customer_views.my_bills, name="my_bills"),
    path('message_view/<str:message>/', customer_views.message_view, name="message_view"),


    #work manager

    path('workmanager_dash', workmanager_views.dash, name="workmanager_dash"),
    path('schedule_work', workmanager_views.schedule_work, name="schedule_work"),
    path('my_appointments', workmanager_views.my_appointments, name="my_appointments"),
    path('works', workmanager_views.works, name="works"),
    path('delete_sch/<int:id>/', workmanager_views.delete_sch, name="delete_sch"),
    path('update_sch/<int:id>/', workmanager_views.update_sch, name="update_sch"),
    path('accept_app/<int:id>/', workmanager_views.accept_app, name="accept_app"),
    path('reject_app/<int:id>/', workmanager_views.reject_app, name="reject_app"),

]

