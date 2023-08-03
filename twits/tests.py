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
from .models import Twit, Comment
from accounts.models import CustomUser



class TwitTests(TestCase):
    """twit tests"""
    @classmethod
    def setUpTestData(cls):
        """set up initial test data"""
        cls.custom_user = get_user_model().objects.create_user(
            username = "testuser1", 
            email = "test@tests.net", 
            password = "secret",
            date_of_birth = "2023-01-01"
        )

        cls.twit = Twit.objects.create(
            author = cls.custom_user,
            body = "my test twit",
            image_url = "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg",
        )
        
        cls.comment = Comment.objects.create(
            twit = cls.twit,
            author = cls.custom_user,
            body = "test comment"
        )

    def test_user(self):
        self.assertEqual(self.custom_user.username, "testuser1")
        self.assertEqual(self.custom_user.date_of_birth, "2023-01-01")

    def test_twit(self):
        self.assertEqual(self.twit.author.username, "testuser1")
        self.assertEqual(self.twit.body, "my test twit")
        self.assertEqual(self.twit.image_url, "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg")
    
    
    def test_twit_create_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.post(
            reverse( "twit_new"),
            {
                "author": self.custom_user.pk,
                "body": "my test twit for create view",
                "image_url": "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.last().body, "my test twit for create view")
        self.assertEqual(Twit.objects.last().image_url, "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg")
        


        
        
        
    def test_twit_detail_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
        no_response = self.client.get("/1000/")
        self.assertEqual(no_response.status_code, 404)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my test twit")
        self.assertTemplateUsed(response, "twit_detail.html")
        self.assertContains(response, "testuser1")
        self.assertContains(response, '<img src="https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg" class="img-fluid" alt="">')
        self.assertContains(response, "test comment")
        # might not need these two:
        self.twit.likes.set([self.custom_user,])
        self.assertEqual(self.twit.likes.count(), 1)
    
    def test_twit_like_view(self):                
        self.client.force_login(self.custom_user)
        # twit should have 0 likes in the database     
        self.assertEqual(self.twit.likes.count(), 0)
        # call like url to add like
        self.client.get("/1/like/?twit_id=1&twit_action=like")
        # twit should now show 1 like in the database
        self.assertEqual(self.twit.likes.count(), 1)
        # test that custom_user exists in likes table
        self.assertTrue(self.twit.likes.contains(self.custom_user))
        # unlike twit
        self.client.get("/1/like/?twit_id=1&twit_action=unlike")
        # twit should now have 0 likes
        self.assertEqual(self.twit.likes.count(), 0)
        # test that custom_user no longer in likes table
        self.assertFalse(self.twit.likes.contains(self.custom_user))



    def test_twit_update_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.post(
            reverse("twit_edit", kwargs={"pk": self.twit.pk}),
            {
                "body": "updated twit",
            },
            )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.last().body, "updated twit")
        self.assertEqual(Twit.objects.last().image_url, "")

    def test_twit_delete_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.post(
            reverse("twit_delete", args="1")
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Twit.objects.count(), 0)
    
    def test_twit_list_view(self):
        """Test url exists at correct location list view (home page)"""
        self.client.force_login(self.custom_user)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "New Twit")
        # testing that user name shows up in side bar
        self.assertContains(response, "testuser1")

    def test_login_required_twit_list_view(self):
        """test login required mixin for list view"""
        response = self.client.get(reverse("home"), follow=True)
        # user is not logged in at this point, so it should redirect to login view
        self.assertRedirects(response, "/accounts/login/?next=/")  
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_required_twit_detail_view(self):
        """test login required mixin for detail view"""
        response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/1/")  
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertFalse(response.context['user'].is_authenticated)
        
    def test_login_required_twit_create_view(self):
        """test login required mixin for create view"""
        response = self.client.get(reverse("twit_new"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/new/")  
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_required_twit_update_view(self):
        """test login required mixin for update view"""
        response = self.client.get(reverse("twit_edit", kwargs={"pk": self.twit.pk}), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/1/edit/")  
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_login_required_twit_delete_view(self):
        """test login required mixin for delete view"""
        response = self.client.get(reverse("twit_delete", kwargs={"pk": self.twit.pk}), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/1/delete/")  
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "registration/login.html")
        self.assertFalse(response.context['user'].is_authenticated)

    def test_user_passes_test_edit_view(self):
        """test user passes test mixin for edit view"""
        alt_test_user = get_user_model().objects.create_user(
            username = "testuser2", 
            email = "test2@tests.net", 
            password = "secret2",
            date_of_birth = "2023-03-03"
        )
        self.client.force_login(alt_test_user)
        response = self.client.get(reverse("twit_edit", kwargs={"pk": self.twit.pk}))
        self.assertEqual(response.status_code, 403)

    def test_user_passes_test_delete_view(self):
        """test user passes test mixin for delete view"""
        alt_test_user = get_user_model().objects.create_user(
            username = "testuser2", 
            email = "test2@tests.net", 
            password = "secret2",
            date_of_birth = "2023-03-03"
        )
        self.client.force_login(alt_test_user)
        response = self.client.get(reverse("twit_delete", kwargs={"pk": self.twit.pk}))
        self.assertEqual(response.status_code, 403)
        
        

# Need tests for: CommentForm, and UserProfileViews.

class CommentTests(TestCase):
    """comment tests"""
    @classmethod
    def setUpTestData(cls):
        """set up initial test data"""
        cls.custom_user = get_user_model().objects.create_user(
            username = "testuser2", 
            email = "test@tests.net", 
            password = "secret",
            date_of_birth = "2023-01-01"
        )

        cls.twit = Twit.objects.create(
            author = cls.custom_user,
            body = "my second test twit",
            image_url = "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg",
        )

        cls.test_comment = Comment.objects.create(
            author = cls.custom_user,
            twit = cls.twit,
            body = "class method",
        )

        
    
    def test_twit_view(self):
        """test to ensure twit renders on list view"""
        self.client.force_login(self.custom_user)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tweeter")
        self.assertContains(response, "my second test twit")
        self.assertTemplateUsed(response, "home.html")
        
        

    def test_comment_create_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.post(
            reverse("twit_detail", kwargs={"pk": self.twit.pk}),
            {
                "author": self.custom_user.pk,
                "body": "test comment",
            }
        ) 
        # should redirect now
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/1/") # url for twit detail
        # need a different response variable to test that the comment shows on the page
        post_response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
        self.assertEqual(post_response.status_code, 200)
        self.assertContains(post_response, "my second test twit")
        self.assertContains(post_response, "test comment")
        

    def test_comment_update_view(self):
        self.client.force_login(self.custom_user)
        # had to recreate the comment again because the previous comment gets destroyed after "test_comment_create_view" finishes
        comment = Comment.objects.create(
            twit = self.twit,
            author = self.custom_user,
            body = "test comment for update view"
        )
        response = self.client.post(
            reverse("comment_edit", kwargs={"twit_pk": self.twit.pk, "pk": comment.pk }),
            {
                "body": "updated comment",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/1/") # url for twit detail
        # testing that the page renders the new comment
        post_response = self.client.get(reverse("twit_detail", kwargs={"pk": self.twit.pk}))
        self.assertContains(post_response, "updated comment")
        self.assertContains(post_response, "testuser2")
        # testing the comment actually saved in the database
        self.assertEqual(Comment.objects.last().body, "updated comment")       
        self.assertEqual(Comment.objects.last().author.username, "testuser2")
        
    def test_comment_delete_view(self):
        self.client.force_login(self.custom_user)
        comment = Comment.objects.create(
            twit = self.twit,
            author = self.custom_user,
            body = "test comment for delete view"
        )
        self.assertEqual(Comment.objects.count(), 2)
        response = self.client.post(
            reverse("comment_delete", kwargs={"twit_pk": self.twit.pk, "pk": comment.pk })
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
    
    def test_user_passes_test_comment_edit_view(self):
        """test user passes test mixin for edit view"""
        alt_test_user = get_user_model().objects.create_user(
            username = "testuser3", 
            email = "test3@tests.net", 
            password = "secret3",
            date_of_birth = "2023-03-03"
        )
        self.client.force_login(alt_test_user)
        response = self.client.get(reverse("comment_edit", kwargs={"twit_pk": self.twit.pk, "pk": self.test_comment.pk}))
        self.assertEqual(response.status_code, 403)

    def test_user_passes_test_comment_delete_view(self):
        """test user passes test mixin for delete view"""
        alt_test_user = get_user_model().objects.create_user(
            username = "testuser3", 
            email = "test3@tests.net", 
            password = "secret3",
            date_of_birth = "2023-03-03"
        )
        self.client.force_login(alt_test_user)
        response = self.client.get(reverse("comment_delete", kwargs={"twit_pk": self.twit.pk, "pk": self.test_comment.pk}))
        self.assertEqual(response.status_code, 403)


        


