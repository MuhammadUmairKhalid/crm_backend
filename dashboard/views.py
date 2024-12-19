# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

def signin(request):
    return render(request, 'dashboard/signin.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html') 


def agent_form(request):
    return render(request, 'dashboard/agentform.html')

def validate_table(request):
    return render(request, 'dashboard/validatetable.html')  

def validate_form(request):
    return render(request, 'dashboard/validateform.html')  

def change_password(request):
    return render(request, 'dashboard/change-password.html') 

def view_agent(request):
    return render(request, 'dashboard/viewagentform.html') 

def super_user(request):
    return render(request, 'dashboard/superuser.html') 

def add_users(request):
    return render(request, 'dashboard/addingusers.html') 

def view_users(request):
    return render(request, 'dashboard/viewusers.html') 

def edit_user(request):
    return render(request, 'dashboard/edituser.html') 


def logout_view(request):
    logout(request) 
    return redirect('login') 