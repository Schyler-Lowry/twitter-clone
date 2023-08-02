from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from .models import Twit, Comment



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
        

    def test_comment(self):
        self.assertEqual(self.comment.author.username, "testuser1")
        self.assertEqual(self.comment.twit.body, "my test twit")
        self.assertEqual(self.comment.body, "test comment")
    
    def test_twit_create_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.post(
            reverse( "twit_new"),
            {
                "author": self.custom_user.pk,
                "body": "my test twit for create view",
                "image_url": "https://i.pinimg.com/564x/a2/b2/c6/a2b2c68e4d3e4126816424920fcdd4fe.jpg",
                "likes": self.custom_user.pk
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
        self.twit.likes.set([self.custom_user,])
        self.assertEqual(self.twit.likes.count(), 1)
    
    def test_twit_like_view(self):
        pass

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
    
    def test_url_exists_at_correct_location_listview(self):
        """Test url exists at correct location list view (home page)"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        
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

        
    
    def test_twit_list_view(self):
        self.client.force_login(self.custom_user)
        response = self.client.get("/")
        #print(response.content.decode())
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
            }, follow=True 
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my second test twit")
        self.assertContains(response, "test comment")
        

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
            }, follow=True # must be set to true to get to twit detail view that has the comment
        )
        # testing that the page renders the new comment
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "updated comment")
        self.assertContains(response, "testuser2")
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
        self.assertEqual(Comment.objects.count(), 1)
        response = self.client.post(
            reverse("comment_delete", kwargs={"twit_pk": self.twit.pk, "pk": comment.pk })
        )
        self.assertEqual(Comment.objects.count(), 0)


        


