from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('emailSignIn')
        password = request.POST.get('loginPassword')
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your desired route after login
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'signin.html')  # Render your sign-in template
