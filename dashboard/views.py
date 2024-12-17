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




