# Generated by Django 2.1.7 on 2019-06-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0039_auto_20190617_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='desc',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]
