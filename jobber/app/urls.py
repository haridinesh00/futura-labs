from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login_view', views.login_view, name="login_view"),
    path('seeker_register', views.seeker_register, name="seeker_register"),
    path('seeker_dashboard', views.seeker_dashboard, name="seeker_dashboard"),
    path('my_profile', views.my_profile, name="my_profile"),
    path('job_listing', views.job_listing, name="job_listing"),
    path('employer_post_new_job', views.employer_post_new_job, name="employer_post_new_job"),
    path('employer_register', views.employer_register, name="employer_register"),
    path('job_details/<int:id>/', views.job_details, name="job_details"),
]
