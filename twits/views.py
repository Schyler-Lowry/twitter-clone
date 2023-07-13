from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Twit
from .forms import CommentForm

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
        # Attach the article to the new comment.
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

class TwitListView(LoginRequiredMixin, ListView):
    """twit list view"""
    model = Twit
    template_name = 'home.html'

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
    fields = ('body',)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

