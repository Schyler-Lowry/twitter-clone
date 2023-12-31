"""
Schyler Lowry
CIS218
8/3/2023
"""

from django.db import models
from django.conf import settings
from django.urls import reverse

class Twit(models.Model):
    """twit model"""
    body = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank=True,
    )
    image_url = models.CharField(max_length=999, blank=True)

    def __str__(self):
        """Twit as a string"""
        return self.body[:30]
    
    def get_absolute_url(self):
        return reverse('twit_detail', kwargs={'pk': self.pk})
    
    def get_like_url(self):
        """get like url based on pk"""
        return reverse("twit_like", kwargs={'pk': self.pk})

class Comment(models.Model):
    """comment model"""
    twit = models.ForeignKey(
        Twit,
        on_delete = models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    body = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """comment as a string"""
        return self.body[:30]
    