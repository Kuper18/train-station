from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create-user"),
    path("login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("me/", ManageUserView.as_view(), name="user-info"),
]

app_name = "user"
