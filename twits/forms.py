from django import forms


from .models import Comment, Twit

class CommentForm(forms.ModelForm):
    """comment form"""
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your reply, in 140 characters or less.'})
        }

class TwitForm(forms.ModelForm):
    """twit form"""
    class Meta:
        model = Twit
        fields = ("body", "image_url",)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Write your Twit, in 140 characters or less.'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Optional: Enter a link to an image.'})
        }