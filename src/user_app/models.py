from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class Profile(models.Model):
    id_profile = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return f'{self.user.first_name} - {self.user.last_name}'