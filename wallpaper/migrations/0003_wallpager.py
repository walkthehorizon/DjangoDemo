# Generated by Django 2.0.2 on 2018-05-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0002_delete_wallpager'),
    ]

    operations = [
        migrations.CreateModel(
            name='WallPager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('describe', models.TextField(default='', max_length=300)),
                ('url', models.CharField(default='', max_length=50)),
                ('category', models.CharField(choices=[(0, '风景风光'), (1, '动漫游戏'), (2, '美丽文字'), (3, '萌娃萌宠'), (4, '文化节日'), (5, '美食天下')], default='风景风光', max_length=20)),
            ],
        ),
    ]
