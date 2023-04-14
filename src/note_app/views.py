from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import NoteSerializer
from .models import Note

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]