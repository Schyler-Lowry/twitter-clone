"""
Schyler Lowry
CIS218
8/3/2023
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Twit, Comment

admin.site.register(Twit)
admin.site.register(Comment)
