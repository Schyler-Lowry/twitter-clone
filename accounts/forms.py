from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.widgets import NumberInput, DateInput
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """custom user creation form"""
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
                "username",
                "email",
                "date_of_birth",
                # no need to provide pw
            )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomUserChangeForm(UserChangeForm):
    """customer user change form"""
    class Meta(UserChangeForm):
        model = CustomUser
    
        fields = (
            "username",
            "email",
            "date_of_birth",
            "first_name",
            "last_name",
            "avatar",
        )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        
        help_texts = {
            'email': 'Tweeter uses Gravatar to display your profile picture.',
        }
        
        