from rest_framework import serializers
from user_app.serializer import UserSerializer
from post_app.serializer import PostSerializer
from post_app.models import Post
from .models import Phrase


class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Phrase
        fields =['url', 'phrase', 'translation', 'create_at', 'update_at', 'post', 'user']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        phrase = Phrase.objects.create(**validated_data)
        return phrase