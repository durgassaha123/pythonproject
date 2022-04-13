# Generated by Django 4.0.3 on 2022-03-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0021_alter_mymusic_audio_file_alter_mymusic_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='myicons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=3000)),
                ('name', models.CharField(max_length=3000)),
                ('title', models.CharField(max_length=3000)),
                ('csscontentcode', models.CharField(max_length=3000)),
                ('svglink', models.CharField(max_length=3000)),
                ('icontype', models.CharField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'myiconslist',
            },
        ),
    ]
