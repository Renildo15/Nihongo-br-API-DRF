from .models import Phrase
from rest_framework import serializers

class PhraseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Phrase
        fields = ['url','phrase', 'translation', 'create_at', 'update_at', 'post', 'user']