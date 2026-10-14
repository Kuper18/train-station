from rest_framework import generics

from user.serializers.user import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
