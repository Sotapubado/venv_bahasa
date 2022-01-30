from tabnanny import verbose
from accounts.models import CustomUser
from django.db import models

class Salon(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.TextField(verbose_name='タイトル', max_length=40)
    content = models.ImageField(verbose_name='写真１', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ar = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Salon'

    def __str__(self):
        return self.title