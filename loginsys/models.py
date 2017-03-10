from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from store.models import Book
from django.dispatch import receiver
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill
from uuid import uuid4
import os


class UserProfile(models.Model):

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid4(), extension)
        return os.path.join("images/avatars", filename)

    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_file_path,
                               default='images/default_profile_pic.jpg')
    avatar_small = ImageSpecField(source='avatar',
                                  processors=[ResizeToFill(100, 100)],
                                  format='JPEG', options={'quality': 60})
    bio = models.TextField(max_length=500)
    favorites = models.ManyToManyField(Book, related_name='favorite_by')


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
