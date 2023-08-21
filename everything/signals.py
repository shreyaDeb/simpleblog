from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Blogger

@receiver(post_save, sender=User)
def create_or_update_blogger_profile(sender, instance, created, **kwargs):
    if created:
        Blogger.objects.create(user=instance)
    instance.blogger.save()