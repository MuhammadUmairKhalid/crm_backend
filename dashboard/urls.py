from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # Route for the sign-in page
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line for the dashboard
    path('agentform/', views.agent_form, name='agent_form'),  # Path to agent form
    path('submit_agent_form/', views.submit_agent_form, name='submit_agent_form'),  
]