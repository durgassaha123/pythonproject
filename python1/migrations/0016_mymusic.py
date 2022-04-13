# Generated by Django 4.0.3 on 2022-03-19 00:14

from django.db import migrations, models
import python1.models


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0015_myproject_projectd'),
    ]

    operations = [
        migrations.CreateModel(
            name='mymusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='thekoushikdurgas', max_length=200)),
                ('artist', models.CharField(default='thekoushikdurgas', max_length=200)),
                ('image', models.ImageField(blank=True, default='mymusic/pic/default.jpg', null=True, upload_to=python1.models.mymusicpath1)),
                ('audio_file', models.FileField(blank=True, default='mymusic/audio/default.mp3', null=True, upload_to=python1.models.mymusicpath2)),
                ('duration', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mymusiclist',
            },
        ),
    ]
