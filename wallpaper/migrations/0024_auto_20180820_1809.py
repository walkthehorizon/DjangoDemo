# Generated by Django 2.0.5 on 2018-08-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0023_auto_20180820_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='cover2',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='cover3',
        ),
        migrations.AlterField(
            model_name='microuser',
            name='avatar',
            field=models.URLField(blank=True, default='\thttp://wallpager-1251812446.cosbj.myqcloud.com/avatar/default_avatar_2.3104244150576956.jpg'),
        ),
    ]
