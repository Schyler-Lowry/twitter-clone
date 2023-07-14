from django.urls import path
from .views import (
    TwitListView,
    TwitCreateView,
    TwitDetailView,
    TwitDeleteView,
    TwitUpdateView,
    TwitLikeView,
)

urlpatterns = [
    path("<int:pk>/", TwitDetailView.as_view(), name="twit_detail"),
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("<int:pk>/like/", TwitLikeView.as_view(), name="twit_like"),
    path("new/", TwitCreateView.as_view(), name="twit_new"),
    path("", TwitListView.as_view(), name="home"),
]