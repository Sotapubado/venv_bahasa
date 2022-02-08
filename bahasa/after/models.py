from tabnanny import verbose
from django.db import models
from accounts.models import CustomUser


# Create your models here.

class After(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    introduction = models.TextField(verbose_name="自己紹介", blank=True, null=True)

    intro_photo = models.ImageField(verbose_name="顔写真", blank=True, null=True)

