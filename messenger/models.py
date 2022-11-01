from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=64)
    is_private = models.BooleanField(default=False)


class Profile(models.Model):
    avatar = models.FileField(upload_to='uploads/', blank=True)


