from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from .models import CustomUser


# Create your tests here.
class AccountsTests(TestCase):
    """tests for login/signup"""

    def test_signup_view(self):
        """test signup view"""
        response = self.client.post(
            reverse("signup"), 
            {
                "username": "testuser2",
                "password1": "@StrongPW1234",
                "password2": "@StrongPW1234",
            }, 
        )
        
        self.assertEqual(response.status_code, 302)
        
    def test_login_view(self):
        """test login view"""
        
        get_user_model().objects.create_user(username="testuser2", password="@StrongPW1234")
        response = self.client.post(reverse("login"), 
            {
                "username": "testuser2",
                "password": "@StrongPW1234"
            }
            , follow=True)
        self.assertTrue(response.context['user'].is_authenticated)