# Generated by Django 4.0.3 on 2022-03-14 20:00

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0014_alter_myproject_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='projectd',
            field=computed_property.fields.ComputedCharField(compute_from='project_d', default='0', editable=False, max_length=150),
        ),
    ]
