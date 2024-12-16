from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # Route for the sign-in page
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line for the dashboard

]