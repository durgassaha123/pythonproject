# Generated by Django 4.0 on 2022-02-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0004_alter_passwords_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='mydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='thekoushikdurgas', max_length=200)),
                ('subject', models.CharField(default='thekoushikdurgas', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mydetailslist',
            },
        ),
    ]
