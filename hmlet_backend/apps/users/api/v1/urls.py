from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from hmlet_backend.apps.users.user_views import UserView

urlpatterns = [
    path(
    "register/",
    UserView.as_view({"post": "register_user"}),
    name="register",
    ),
    path(
    "login/",
    UserView.as_view({"post": "login_user"}),
    name="login",
    ),
    # Not in the spec, but free - exchanges a refresh token for a new access token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
