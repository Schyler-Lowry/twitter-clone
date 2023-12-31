"""
Schyler Lowry
CIS218
8/3/2023
"""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """custom user admin to register the custom user model in the admin"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "date_of_birth",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("date_of_birth",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("date_of_birth",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
