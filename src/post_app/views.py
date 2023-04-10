from .serializer import PostSerializer
from .models import Post
from phrase_app.models import Phrase
from phrase_app.serializers import PhraseSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-create_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def phrase_list(self, request, pk=None):
        post =  self.get_object()
        phrases = Phrase.objects.filter(post=post)
        serializer = PhraseSerializer(phrases, many = True, context={'request': request})

        return Response(serializer.data)