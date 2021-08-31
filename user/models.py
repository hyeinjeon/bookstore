from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser): 
    profilePic = models.ImageField(upload_to="user/", blank=True, null=True)
    introduce =  models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='followings'
        )
