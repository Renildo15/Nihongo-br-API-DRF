from .serializer import UserSerializer, ProfileSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile


class UserViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
   

    def get_queryset(self):
        user = self.request.user
        queryset = Profile.objects.filter(user=user)
        return queryset