from django.contrib.auth.models import AbstractUser

from tabnanny import verbose
from django.db import models


class CustomUser(AbstractUser):
    
    class Meta:
        verbose_name_plural = 'CustomUser'



# Create your models here.

class Account (models.Model):

    introduction = models.TextField(verbose_name="自己紹介", blank=True, null=True)

    icon = models.ImageField(verbose_name="顔写真", blank=True, null=True)

