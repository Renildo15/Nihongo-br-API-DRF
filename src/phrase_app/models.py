from django.db import models
from uuid import uuid4
from post_app.models import Post
from django.contrib.auth.models import User
# Create your models here.


class Phrase(models.Model):
    id_phrase = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    phrase = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="phrases")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phrases" )


    class Meta:
        ordering = ['-create_at']
        verbose_name = "Phrases"
        verbose_name_plural = "Phrases"

    def __str__(self):
        return self.phrase