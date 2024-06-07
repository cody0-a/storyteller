from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(
            unique=True,
            null=False,
            blank=False,
            region="ET",
            
        )
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user
    
 



class Register(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'Register'
        verbose_name_plural = 'Register'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')


    def __str__(self):
        return self.user

class Friend(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    shared_friend = models.BooleanField(default= False)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_shared')

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')

    def __str__(self):
        return self.username
    

class StoryTeller(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    shared_story = models.BooleanField(default= False)
    story = models.TextField
    storyteller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story')

    class Meta:
        verbose_name = 'StoryTeller'
        verbose_name_plural = 'StoryTellers'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')
    
    def __str__(self):
        return self.username
    