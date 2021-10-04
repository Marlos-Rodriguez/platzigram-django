# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Erros Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User

# Local Apps
from users.models import Profile

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def singup_view(request):
    """Sign Up view"""
    if request.method == 'POST':
        # Get User data
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        # Create user or return error
        try:
            user = User.objects.create_user(
                username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        # Add aditional Info
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        # Create Profile from user
        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """LogOut User"""
    logout(request)
    return redirect('login')
