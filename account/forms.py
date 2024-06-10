from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django import forms


class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone Number')
    city = forms.CharField(label='City')
    state = forms.CharField(label='State')
    zipcode = forms.CharField(label='Zipcode')
    country = forms.CharField(label='Country')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number', 'city', 'state', 'zipcode', 'country')

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

class StoryCommentForm(forms.ModelForm):
    class Meta:
        model = StoryComment
        fields =['comment_text']


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields =['title', 'content']
        
class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label=_("Old password"), strip=False, widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("New password confirmation"), strip=False, widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user    

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_("Email"), max_length=254)  

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise ValidationError("There is no user registered with the specified email address.")
        return email

    def save(self, domain_override=None, email=None, **kwargs):
        email = self.cleaned_data["email"]
        email_field_name = User.get_email_field_name()
        for user in User.objects.filter(**{email_field_name: email}):
            user.set_password(self.cleaned_data["new_password1"])
            user.save()


        return user
    