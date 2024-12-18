from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),  # Route for the sign-in page
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line for the dashboard
    path('agentform/', views.agent_form, name='agent_form'),  # Path to agent form
    path('submit_agent_form/', views.submit_agent_form, name='submit_agent_form'),  
    path('validate_form/', views.validate_form, name ='validate_form'),
    path('validate_table/', views.validate_table, name = 'validate_table'),
    path('change_password/', views.change_password, name = 'change_password'),

]