from .serializer import UserSerializer, ProfileSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.decorators import action
from rest_framework.response import Response
from post_app.models import Post
from post_app.serializer import PostSerializer


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
    @action(detail=True, methods=['get'])

    def post_list(self, request, pk=None):
        profile = self.get_object()
        post = Post.objects.filter(user=profile.user)
        serializer = PostSerializer(post, many=True, context={"request":request})

        return Response(serializer.data)
