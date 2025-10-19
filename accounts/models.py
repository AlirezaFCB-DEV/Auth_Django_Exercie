from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#! If you just want to add a few fields, or slightly modify existing fields, use AbstractUser.
class User (AbstractUser) :
    """
    User model
    """
    phone = models.CharField(max_length=20 , blank=True , null=True)
    avatar = models.ImageField(upload_to="avatars/" , blank=True , null=True)
    
    def __str__(self):
        return super().username