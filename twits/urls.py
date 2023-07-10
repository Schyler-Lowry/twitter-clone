from django.urls import path
from .views import (
    TwitListView,
)

urlpatterns = [
    path("", TwitListView.as_view(), name="twit_list")
]