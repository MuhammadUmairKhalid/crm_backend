# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def signin(request):
    return render(request, 'dashboard/signin.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html') 


def agent_form(request):
    if request.method == 'POST':
        # Process form data here if needed
        pass
    return render(request, 'dashboard/agentform.html')

def submit_agent_form(request):
    return render(request, 'dashboard/agent_form')


def validate_table(request):
    return render(request, 'dashboard/validatetable.html')  

def validate_form(request):
    return render(request, 'dashboard/validateform.html')  

def change_password(request):
    return render(request, 'dashboard/change-password.html') 
