# Generated by Django 4.0 on 2022-02-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='link',
            field=models.URLField(default='http://google.com'),
        ),
    ]
