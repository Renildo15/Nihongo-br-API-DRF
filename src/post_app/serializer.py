from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ['url', 'grammar', 'connection', 'note', 'level', 'create_at', 'update_at', 'user']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        post = Post.objects.create(**validated_data)
        return post