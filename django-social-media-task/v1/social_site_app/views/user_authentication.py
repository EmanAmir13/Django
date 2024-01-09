from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from social_site_app.models.profile import UserProfile
from v1.social_site_app.forms import UserForm


@login_required(login_url='/')
def welcome(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    return render(request, 'v1/welcome.html', {'user_profile': user_profile})


def register_user(request):
    form = UserForm()
    if not request.method == 'POST':
        return render(request, "v1/register.html", {'form': form})

    form = UserForm(request.POST)
    if not form.is_valid():
        messages.error(request, f"{form.errors}")
        return redirect(reverse('register_user'))

    form.save()
    messages.success(request, 'Registration successful. Welcome back!')
    return redirect(reverse('sign_in'))


def sign_in(request):
    if not request.method == 'POST':
        return render(request, 'v1/login.html')

    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, 'Login successful. Welcome back!')
        return redirect(reverse('welcome'))
    else:
        messages.error(request, "Invalid credentials. Please try again.")
        return redirect(reverse('sign_in'))


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')
