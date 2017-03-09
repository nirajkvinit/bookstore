from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from store.models import Book
from django.dispatch import receiver
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatars/')
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
