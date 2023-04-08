from .models import Phrase
from rest_framework import serializers

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post-phrases', read_only=True)
    user = serializers.HyperlinkedRelatedField(
        view_name='user-phrases', read_only=True)

    class Meta:
        model = Phrase
        fields = ['url','phrase', 'translation', 'create_at', 'update_at', 'post', 'user']