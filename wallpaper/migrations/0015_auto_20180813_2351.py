# Generated by Django 2.0.5 on 2018-08-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0014_auto_20180812_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='cover_2',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='subject',
            name='cover_3',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='microuser',
            name='avatar',
            field=models.URLField(blank=True, default='\thttp://wallpager-1251812446.cosbj.myqcloud.com/avatar/default_avatar_9.969719490204284.jpg', null=True),
        ),
    ]
