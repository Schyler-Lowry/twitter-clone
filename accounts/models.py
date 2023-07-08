from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    """custom user model"""
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter your date of birth.")

    def get_absolute_url(self):    
        return reverse('user_profile', kwargs={'pk': self.pk})
    

