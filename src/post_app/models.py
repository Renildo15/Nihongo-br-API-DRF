from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    LEVEL_CHOICES = (
        ('n5', 'N5'),
        ('n4', 'N4'),
        ('n3', 'N3'),
        ('n2', 'N2'),
        ('n1', 'N1'),
        ('unknow', 'Unknow'),
    )

    id_post = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    grammar = models.CharField(max_length=250)
    connection = models.CharField(max_length=250)
    level = models.CharField(max_length=250, choices=LEVEL_CHOICES, default='n5')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['grammar']
        verbose_name = "Posts"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'{self.grammar}'