from django.urls import path
from .views import (
    TwitListView,
    TwitCreateView,
    TwitDetailView,
    TwitDeleteView,
    TwitUpdateView,
    TwitLikeView,
    CommentUpdateView,
    CommentDeleteView,
    #TwitListWithCommentCreateView,
)
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    
    path("<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("<int:twit_pk>/comment/edit/<int:pk>/", CommentUpdateView.as_view(), name="comment_edit"),
    path("<int:twit_pk>/comment/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment_delete"),
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("new/", TwitCreateView.as_view(), name="twit_new"),
    #path("testing/", TwitListWithCommentCreateView.as_view(), name="testing"),
    path("", TwitListView.as_view(), name="home"),
]