from django.db import models
# importing default user
from django.contrib.auth.models import User

class Streamer(User):
    class Meta:
        verbose_name = "Streamer"
        verbose_name_plural = "Streamers"

    twitch_link = models.URLField(max_length=50)

class Viewer(User):
    class Meta:
        verbose_name = "Viewer"
        verbose_name_plural = "Viewers"
    
    avatar_image = models.URLField() # twitch profile picture url
    biography = models.TextField()

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=100)
    viewer = models.ManyToManyField(Viewer, related_name='category')
    streamer = models.ManyToManyField(Streamer, related_name='category')

class Trait(models.Model):
    name = models.CharField(max_length=40)
    viewer = models.ManyToManyField(Viewer, related_name='trait')
    streamer = models.ManyToManyField(Streamer, related_name='trait')

class Language(models.Model):
    name = models.CharField(max_length=20)
    viewer = models.ManyToManyField(Viewer, related_name='language')
    streamer = models.ManyToManyField(Streamer, related_name='language')



