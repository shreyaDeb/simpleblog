from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.


class Blogger(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")  # Change the default value as needed

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)

class Comment(models.Model):
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]  # Display a truncated comment content


@receiver(post_save, sender=User)
def create_blogger_profile(sender, instance, created, **kwargs):
    if created:
        Blogger.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_blogger_profile(sender, instance, **kwargs):
    instance.blogger.save()
