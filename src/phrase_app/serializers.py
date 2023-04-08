from rest_framework import serializers
from .models import Phrase


class PhraseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Phrase
        fields = '__all__'