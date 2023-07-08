from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        )