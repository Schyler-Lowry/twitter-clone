from django.urls import path
from .views import SignUpView, UserProfileView, UserProfileChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
        path('profile/<int:pk>/edit', UserProfileChangeView.as_view(), name='user_change_profile'),
        path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile"),
]