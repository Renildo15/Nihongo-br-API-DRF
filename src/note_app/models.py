from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from post_app.models import Post
# Create your models here.

class Note(models.Model):
    id_note =  models.UUIDField(primary_key=True, default=uuid4, editable=False)
    note = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="notes")

    class Meta:
        ordering = ['note']
        verbose_name = "Notes"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.note
