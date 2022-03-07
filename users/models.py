from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your models here.

def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.error(request, 'User not found.')
            return render(request, 'account/login.html')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.error(request, 'Profile is not verified check your mail.')
            return render(request, 'account/login.html')

        user = authenticate(username=user_obj.username, password=password)
        if user is None:
            messages.error(request, 'Wrong password.')
            return render(request, 'account/login.html')

        login(request, user)
        return redirect('/')

    return render(request, 'account/login.html')
