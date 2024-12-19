from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),  # Route for the sign-in page
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this line for the dashboard
    path('agentform/', views.agent_form, name='agent_form'),  # Path to agent form 
    path('validate_form/', views.validate_form, name ='validate_form'),
    path('validate_table/', views.validate_table, name = 'validate_table'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),
    path('view_agent/', views.view_agent, name = 'view_agent'),
    path('super_user/', views.super_user, name = 'super_user'),
    path('add_users/', views.add_users, name = 'add_users'),
    path('view_users/', views.view_users, name = 'view_users'),
    path('edit_user/', views.edit_user, name = 'edit_user'),
    

]