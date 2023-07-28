from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormMixin, BaseCreateView

from django.urls import reverse_lazy, reverse

from .models import Twit, Comment
from .forms import CommentForm

"""
Posible TODO: Create a custom "list view" that enables comment posting from the list view home page.
              The purpose of this would be to remove the necessity of going to the twit detail page in order to make a comment.
"""
class CommentCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy("testing")
    form_class = CommentForm
    template_name = "testing_page.html"
    
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
        return context




class TwitDetailView(LoginRequiredMixin, View):
    """twit detail view"""
    def get(self, request, *args, **kwargs):
        """doing GET request"""
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """doing POST request"""
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)

class CommentGetView(DetailView):
    """comment get view"""
    model = Twit
    template_name = "twit_detail.html"
    
    def get_context_data(self, **kwargs):
        """override context data to send to template"""
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class CommentPostView(SingleObjectMixin, FormView):
    model = Twit
    form_class = CommentForm
    template_name = "twit_detail.html"

    def post(self, request, *args, **kwargs):
        # Get the Twit object associated with the pk in the url
        self.object = self.get_object()
        # Do work parent would have done
        return super().post(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        """create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to False,
        # because we don't want the form to actually fully save the model to the db yet.
        comment = form.save(commit=False)
        # Attach the twit to the new comment.
        comment.twit = self.object
        # Attach the logged in user to the new comment.
        comment.author = self.request.user
        # now we call save() to commit the comment to the DB
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """get the success url"""
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk": twit.pk})
    
    
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """twit update view"""
    model = Comment
    form_class = CommentForm
    template_name = "comment_edit.html"
    

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    def get_success_url(self):
        """get the success url"""
        comment = self.get_object()
        return reverse("twit_detail", kwargs={"pk": comment.twit.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """twit update view"""
    model = Comment
    
    template_name = "comment_delete.html"
    #success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    def get_success_url(self):
        """get the success url"""
        comment = self.get_object()
        return reverse("twit_detail", kwargs={"pk": comment.twit.pk})
    # def get_success_url(self):
    #     """get the success url"""
    #     comment = self.get_object()
    #     return reverse("twit_detail", kwargs={"pk": comment.twit.pk})

class TwitListView(LoginRequiredMixin, ListView):
    """twit list view"""
    model = Twit
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(TwitListView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context
    

    

class TwitCreateView(LoginRequiredMixin, CreateView):
    """twit create view"""
    model = Twit
    template_name = "twit_new.html"
    
    fields = (
        "body",
        "image_url",
    )
    def form_valid(self, form):
        """override form valid method"""
        form.instance.author = self.request.user
        return super().form_valid(form)

# class TwitDetailView(LoginRequiredMixin, DetailView):
#     """twit detail view"""
#     model = Twit
#     template_name = "twit_detail.html"

class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """twit delete view"""
    model = Twit
    template_name = "twit_delete.html"
    success_url = reverse_lazy('home')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """twit update view"""
    model = Twit
    template_name = "twit_edit.html"
    fields = ('body','image_url',)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class TwitLikeView(LoginRequiredMixin, View):
    """twit like view"""
    def get(self, request, *args, **kwargs):
        """GET request"""

        # Get out the data from the GET request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        if not twit_id or not twit_action:
            return JsonResponse(
                {
                    "success": False,
                }
            )

        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":
            # Do like stuff
            twit.likes.add(request.user)
            #twit.save()  # might not need this method
        else:
            # Do unlike stuff
            twit.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )