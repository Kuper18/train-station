from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import CreateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create-user"),
    path("login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

app_name = "user"
