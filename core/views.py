# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def signin(request):
    # Hardcoded email and password for testing purposes
    valid_email = 'user@example.com'
    valid_password = 'password123'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the entered email and password match the valid credentials
        if email == valid_email and password == valid_password:
            return redirect('dashboard')  # Redirect to the dashboard on successful login
        else:
            messages.error(request, "Invalid email or password.")  # Display error if credentials are incorrect
    
        # If authentication fails
        return render(request, 'dashboard/signin.html', {'error': 'Invalid credentials. Please try again.'})
    return render(request, 'dashboard/signin.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')  # Assuming you have this template

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def agent_form(request):
    if request.method == 'POST':
        # Process form data here if needed
        pass
    return render(request, 'dashboard/agentform.html')  # Ensure this path matches your template structure

def submit_agent_form(request):
    """Handle the form submission"""
    if request.method == 'POST':
        # Extract form data
        birth_state = request.POST.get('birth_state')
        phone = request.POST.get('phone')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        zip_code = request.POST.get('zip_code')
        dob = request.POST.get('dob')
        weight = request.POST.get('weight')
        insurance_company = request.POST.get('insurance_company')
        ssn = request.POST.get('ssn')
        beneficiary_details = request.POST.get('beneficiary_details')
        health_conditions = request.POST.get('health_conditions')
        doctor_name = request.POST.get('doctor_name')
        doctor_address = request.POST.get('doctor_address')
        bank_name = request.POST.get('bank_name')
        routing_no = request.POST.get('routing_no')
        account_no = request.POST.get('account_no')
        account_type = request.POST.get('account_type')

        # Add basic validation or form processing logic here
        if not phone or not zip_code or not routing_no or not account_no:
            messages.error(request, "Please fill in the required fields.")
            return redirect('agent_form')

        # If the form is valid, you can save the data or process it
        # For demonstration purposes, we'll just show a success message
        messages.success(request, "Form submitted successfully!")
        return redirect('agent_form')  # Redirect back to the form page after successful submission

    return redirect('agent_form')  # If the request method is not POST, redirect to the form

def validate_table(request):
    return render(request, 'dashboard/validatetable.html')  

def validate_form(request):
    return render(request, 'dashboard/validateform.html')  

def change_password(request):
    return render(request, 'dashboard/change-password.html') 