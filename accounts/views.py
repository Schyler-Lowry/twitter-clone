"""
Schyler Lowry
CIS218
8/3/2023
"""

from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from twits.forms import CommentForm
from twits.models import Twit
from .models import CustomUser

class SignUpView(CreateView):
    """signup view"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserProfileView(LoginRequiredMixin, DetailView):
    """user's profile view"""
    model = CustomUser
    template_name = "registration/user_profile.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[]

class UserProfileChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """view for changing user profile info"""
    form_class = CustomUserChangeForm
    model = CustomUser
    #success_url = reverse_lazy("user_profile")
    template_name = "registration/user_change_profile.html"
    
    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk

class CommentCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy("testing")
    form_class = CommentForm
    template_name = "registration/user_profile.html"
    
    def form_valid(self, form, **kwargs):
        """create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to False,
        # because we don't want the form to actually fully save the model to the db yet.
        comment = form.save(commit=False)
        # Attach the twit to the new comment.
        id = self.request.POST.get("twit_id")
        comment.twit = Twit.objects.get(pk=id)
        # Attach the logged in user to the new comment.
        comment.author = self.request.user
        # now we call save() to commit the comment to the DB
        comment.save()
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        """override context data to send to template"""
        context = super().get_context_data(**kwargs)
        context["twit_list"] = Twit.objects.all()
        #pk = self.request.GET.get("pk")
        context["customuser"] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context