"""
Schyler Lowry
CIS218
8/3/2023
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Twit, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    


class TwitAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    fields = ['body', 'image_url','author', 'likes', 'created', 'updated',]
    readonly_fields = ('created', 'updated',)

admin.site.register(Twit, TwitAdmin)
admin.site.register(Comment)
