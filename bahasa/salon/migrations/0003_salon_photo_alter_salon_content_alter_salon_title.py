# Generated by Django 4.0.1 on 2022-01-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_alter_salon_content_alter_salon_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='title',
            field=models.CharField(max_length=40, verbose_name='タイトル'),
        ),
    ]
