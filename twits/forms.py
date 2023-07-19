from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Comment
        fields = ("body",)

