"""
Schyler Lowry
CIS218
8/3/2023
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from .models import CustomUser


# Create your tests here.
class AccountsTests(TestCase):
    """tests for login/signup"""
    @classmethod
    def setUpTestData(cls):
        """set up initial test data"""
        cls.custom_user = get_user_model().objects.create_user(
            username = "testuser1", 
            email = "test@tests.net", 
            password = "secret",
            date_of_birth = "2023-01-01"
        )

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

    def test_user_update_view(self):
        """test update user profile view"""
        self.client.force_login(self.custom_user)
        # self.assertEqual(CustomUser.objects.count(),1)
        response = self.client.post(
            reverse("user_change_profile", kwargs={"pk": self.custom_user.pk}),
            {
                "username": "testuser1",
                "first_name": "Test",
                "last_name": "User",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/profile/1/")
        #print(response.content.decode())
        post_response = self.client.get(reverse("user_profile", kwargs={"pk": self.custom_user.pk}))
        self.assertTemplateUsed(post_response, "registration/user_profile.html")
        self.assertEqual(CustomUser.objects.last().first_name, "Test")
        self.assertContains(post_response, "Name: Test User")
