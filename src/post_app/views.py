from .serializer import PostSerializer
from .models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-create_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]