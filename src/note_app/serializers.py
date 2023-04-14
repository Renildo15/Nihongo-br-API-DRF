from rest_framework import serializers
from .models import Note
from user_app.serializer import UserSerializer
from post_app.serializer import PostSerializer
from post_app.models import Post


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset = Post.objects.all())

    class Meta:
        model = Note
        fields = ['url', 'note', 'user', 'post']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        note = Note.objects.create(**validated_data)
        return note