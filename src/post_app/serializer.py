from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.Serializer):

    LEVEL_CHOICES = (
        ('n5', 'N5'),
        ('n4', 'N4'),
        ('n3', 'N3'),
        ('n2', 'N2'),
        ('n1', 'N1'),
        ('unknow', 'Unknow'),
    )

    id_post = serializers.UUIDField(read_only=True)
    grammar = serializers.CharField(max_length=250)
    connection = serializers.CharField(max_length=250)
    note = serializers.CharField(allow_blank=True, allow_null=True)
    level = serializers.ChoiceField(choices=LEVEL_CHOICES, default='n5')
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post