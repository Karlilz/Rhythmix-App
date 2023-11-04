from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField( verbose_name='email', max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    username = models.CharField(max_length=500, unique=True)

    