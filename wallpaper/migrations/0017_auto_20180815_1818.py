# Generated by Django 2.0.5 on 2018-08-15 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0016_auto_20180814_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='support_people',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='microuser',
            name='avatar',
            field=models.URLField(blank=True, default='\thttp://wallpager-1251812446.cosbj.myqcloud.com/avatar/default_avatar_11.018543097899297.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallpapers', to=settings.AUTH_USER_MODEL),
        ),
    ]
