from django import forms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .forms import *
import channels
from .serializers import *
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserCreationForm, LoginForm, ChangeEmailForm, StoryForm, StoryCommentForm
from .models import *

def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user_data = {
                'username': user.username,
                'email': user.email,
                'created_at': user.created_at.isoformat(),
                'updated_at': user.updated_at.isoformat()
            }
            return JsonResponse(user_data)
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

@login_required
def logout_user(request):
    logout(request)
    return redirect('account:login')

@login_required
def change_password(request):
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
    return render(request, 'account/change_password.html', {'form': form})

@login_required
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password was reset successfully')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordResetForm()
    return render(request, 'account/reset_password.html', {'form': form})

@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email was successfully updated!')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangeEmailForm(instance=request.user)
    return render(request, 'account/change_email.html', {'form': form})

@login_required
def user_update(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('account:user_detail')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm(instance=user)
    return render(request, 'account/user_update.html', {'form': form})

@login_required
def user_detail(request):
    user = get_object_or_404(User, pk=request.user.id)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'account/user_detail.html', {'profile': profile})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'account/user_list.html', {'users': users})

@login_required
def set_story_like(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    StoryLike.objects.get_or_create(story=story, user=request.user)

@login_required
def story_comment_like(request, comment_id):
    story_comment = get_object_or_404(StoryComment, id=comment_id)
    StoryCommentLike.objects.get_or_create(story_comment=story_comment, user=request.user)

@login_required
def unlike_story(request, story_id):
    story_like = StoryLike.objects.filter(story_id=story_id, user=request.user).first()
    if story_like:
        story_like.delete()

@login_required
def unlike_comment_story(request, comment_id):
    story_comment_like = StoryCommentLike.objects.filter(story_comment_id=comment_id, user=request.user).first()
    if story_comment_like:
        story_comment_like.delete()

@login_required
def create_story_comment(request, story_id):
    if request.method == "POST":
        form = StoryCommentForm(request.POST)
        if form.is_valid():
            story = get_object_or_404(Story, id=story_id)
            story_comment = form.save(commit=False)
            story_comment.story = story
            story_comment.author = request.user
            story_comment.save()
            return redirect('account:story_detail', story_id=story.id)
        else:
            return render(request, 'account/create_story_comment.html', {'form': form})
    else:
        form = StoryCommentForm()
    return render(request, 'account/create_story_comment.html', {'form': form})

@login_required
def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'account/story_detail.html', {'story': story})

@login_required
def edit_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your story was successfully updated!')
            return redirect('account:story_detail', story_id=story.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = StoryForm(instance=story)
    return render(request, 'account/edit_story.html', {'form': form})

@login_required
def delete_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    story.delete()
    return redirect('account:story_list')

@login_required
def update_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Story details updated successfully.')
            return redirect('account:story_detail', story_id=story.id)
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = StoryForm(instance=story)
    return render(request, 'account/update_story.html', {'form': form})

@login_required
def share_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        user_ids = request.POST.getlist('share_users')
        for user_id in user_ids:
            try:
                user = User.objects.get(pk=user_id)
                SharedStory.objects.create(story=story, user=user, shared_by=request.user)
            except User.DoesNotExist:
                pass
        messages.success(request, f"Story '{story.title}' has been shared.")
        return redirect('account:story_detail', story_id=story.id)
    users = User.objects.exclude(pk=request.user.pk)
    return render(request, 'account/share_story.html', {'story': story, 'users': users})
class ShareStoryView(generics.CreateAPIView):
    queryset = SharedStory.objects.all()
    serializer_class = SharedStorySerializer
    permission_classes = [IsAuthenticated]

class ShareCommentView(generics.CreateAPIView):
    queryset = SharedComment.objects.all()
    serializer_class = SharedCommentSerializer
    permission_classes = [IsAuthenticated]