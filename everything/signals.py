from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blogger

@receiver(post_save, sender=User)
def create_blogger_profile(sender, instance, created, **kwargs):
    if created and not Blogger.objects.filter(user=instance).exists():
        Blogger.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_blogger_profile(sender, instance, **kwargs):
    if not Blogger.objects.filter(user=instance).exists():
        instance.blogger.save()