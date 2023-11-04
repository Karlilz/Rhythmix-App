from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    name = models.CharField(max_length=100)

'''
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
'''