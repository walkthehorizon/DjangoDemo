# Generated by Django 2.1.7 on 2019-04-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0031_auto_20190416_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microuser',
            name='avatar',
            field=models.URLField(blank=True, default='\thttp://wallpager-1251812446.cosbj.myqcloud.com/avatar/default_avatar_10.85579595408809.jpg'),
        ),
    ]
