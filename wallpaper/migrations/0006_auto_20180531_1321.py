# Generated by Django 2.0.2 on 2018-05-31 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallpaper', '0005_auto_20180530_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallpager',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='wallpager',
            name='highlighted',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='wallpager',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='wallpaper', to=settings.AUTH_USER_MODEL),
        ),
    ]
