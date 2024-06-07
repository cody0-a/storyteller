from django.core.exceptions import ValidationError
from django.core.validators  import MinValueValidator,MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=254)
    shared_friend = models.BooleanField(default= False)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friend_shared')

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')

    def __str__(self):
        return self.username
    

class StoryTeller(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    shared_story = models.BooleanField(default= False)
    story = models.TextField
    storyteller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='storytellers')

    class Meta:
        verbose_name = 'StoryTeller'
        verbose_name_plural = 'StoryTellers'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')
    
    def __str__(self):
        return self.username

class Story(models.Model):
    """
    Model for storing user-submitted stories.
    """
    title = models.CharField(max_length= 100,
                             validators=[MinValueValidator,
                                        MaxValueValidator
                                        ])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.CharField(max_length=100)
    categories = models.ManyToManyField('Category', related_name='stories')
    tags = models.CharField(max_length=200)
    image = models.ImageField(upload_to='story_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if not self.categories.exists():
            raise ValidationError('At least one category must be selected.')
        
        if self.categries.exists() > 3:
            raise ValidationError('maximum number of categories must be at most 2')
        
        super().clean()


class StoryComment(models.Model):
    """
    Model for storing comments on stories.
    """
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.story.title}"

class Category(models.Model):
    """
    Model for storing story categories.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
class StoryLike(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =('story','user')

class StoryCommentLike(models.Model):
    story_comment = models.ForeignKey(StoryComment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('story_comment', 'user')


class StoryShare(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='shared_stories')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shared_stories')
    shared_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shared_by')
    shared_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('story', 'user')

    def __str__(self):
        return f"{self.shared_by.username} shared '{self.story.title}' with {self.user.username}"
    def is_story_read(self):
        return self.story.read_by.filter(id=self.user.id).exists()
