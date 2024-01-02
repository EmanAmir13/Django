from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from v1.social_site_app.forms import UserAdminCreationForm


def welcome(request):
    return render(request, "v1/welcome.html")


def register_user(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Welcome back!')
            return redirect(reverse('custom_login'))
        else:
            messages.error(request, f"{form.errors}")
            return redirect(reverse('register_user'))

    return render(request, "v1/register.html", {'form': form})


def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect(reverse('welcome'))
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect(reverse('custom_login'))

    return render(request, 'v1/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
