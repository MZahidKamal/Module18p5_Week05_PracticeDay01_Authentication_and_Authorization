from django.shortcuts import render, redirect
from .forms import UserInfoForm, UserInfoUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, f'Welcome {user}! Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserInfoForm()
    context = {'form': form, 'type': 'Sign Up'}
    return render(request, 'user_app/signup.html', context)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}! Login successful!')
                return redirect('show_profile')
            else:
                messages.error(request, 'Account Not Existed.')
                return redirect('signup')
    else:
        form = AuthenticationForm()
    context = {'form': form, 'type': 'Login'}
    return render(request, 'user_app/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


@login_required
def show_user_profile(request):
    profile = User.objects.get(username=request.user.username)
    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
    }
    return render(request, './user_app/show_profile.html', context)


@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = UserInfoUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Your profile information has been updated successfully.')
            return redirect('show_profile')
    else:
        form = UserInfoUpdateForm(instance=request.user)
    context = {'form': form, 'type': 'Edit'}
    return render(request, 'user_app/edit_profile.html', context)


@login_required
def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, 'type': 'Change'}
    return render(request, 'user_app/change_password.html', context)


@login_required
def reset_user_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')
    else:
        form = SetPasswordForm(request.user)
    context = {'form': form, 'type': 'Reset'}
    return render(request, 'user_app/reset_password.html', context)
