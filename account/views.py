from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import JsonResponse
from .models import UserProfile
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ChangeEmailForm, UserCreationForm,LoginForm

def index(request):
    return render(request, 'account/index.html')


import json
from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user_data = {
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'phone': user.phone,
                'address': user.address,
                'city': user.city,
                'state': user.state,
                'zipcode': user.zipcode,
                'country': user.country,
                'gender': user.gender,
                'hobbies': user.hobbies,
                'about': user.about,
                'image': str(user.image),
                'role': user.role,
                'created_at': user.created_at.isoformat(),
                'updated_at': user.updated_at.isoformat()
            }
            return JsonResponse(user_data)
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Optionally, you can also fetch and return user-specific data
            user_profile = UserProfile.objects.get(user=user)
            return JsonResponse({'user': user.username, 'profile': user_profile.to_dict()})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)
    else:
        loginform = LoginForm(request.POST)
        return render(request, 'account/login.html',{'loginform': loginform})
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('account:login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('account:change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'account/change_password.html', {
            'form': form
        })
    else:
        return redirect('account:login')
@login_required
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request, 'password was reset successfully')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('account:reset_password')
    else:
        form = PasswordResetForm(request.user)
        return redirect('account:reset_password')


def reset_password_from_key(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request, 'password was reset successfully')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('account:reset_password')
    else:
        form = PasswordResetForm(request.user)
        return redirect('account:reset_password')

def change_email(request):
    if request.user.is_authenticated:
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email was successfully updated!')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('account:change_email')
    else:
        return redirect('account:login')    


def user_update(request,pk):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        if request.method == 'POST':
            form = UserCreationForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your email was successfully updated!')
                return redirect('account:login')
            else:
                messages.error(request, 'Please correct the error below.')
                return redirect('account:change_email')
        else:
            form = UserCreationForm(instance=user)
            return render(request, 'account/user_update.html', {'form': form})
    else:
        return redirect('account:login')
    
def user_detail(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        if request.method == 'GET':
             profile = get_object_or_404(UserProfile, pk=request.user.id)
             if profile.is_active:
                 return render(request, 'account/user_detail.html', {'profile': profile})
             else:
                 raise Exception('User is not active')
        else:
            return
    else:
        return redirect('account:login')
    
def user_list(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        if users.is_active:

            return render(request, 'account/user_list.html', {'users': users})
        return render(request, 'account/user_list.html', {'users': users})
    else:
        return redirect('account:login')
    
