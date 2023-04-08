from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        post = Post.objects.create(**validated_data)
        return post