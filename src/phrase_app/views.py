from django.shortcuts import render
from .models import Phrase
from django.shortcuts import get_object_or_404
from .serializers import PhraseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PhraseViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Phrase.objects.all()
        serializer = PhraseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Phrase.objects.all()
        phrase = get_object_or_404(queryset, pk=pk)
        serializer = PhraseSerializer(phrase)
        return Response(serializer.data)
