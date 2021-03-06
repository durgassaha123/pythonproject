# Generated by Django 4.0.3 on 2022-03-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0022_myicons'),
    ]

    operations = [
        migrations.CreateModel(
            name='continents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccode', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('name', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'continents',
            },
        ),
        migrations.CreateModel(
            name='countrys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccode', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('value', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('name', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('mcode', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('continents', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'countrys',
            },
        ),
        migrations.CreateModel(
            name='currentacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('name', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('symbolnative', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('decimaldigits', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('rounding', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('code', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('nameplural', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'currentacy',
            },
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('name', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('nativeName', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='thekoushikdurgas', max_length=3000)),
                ('countrys', models.CharField(default='thekoushikdurgas', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.AlterField(
            model_name='mydetails',
            name='title',
            field=models.CharField(default='thekoushikdurgass', max_length=2000),
        ),
    ]
