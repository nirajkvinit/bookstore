from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.AutoOneToOne(User)
    profile_name = models.CharField()
    avatar = models.ImageField()
