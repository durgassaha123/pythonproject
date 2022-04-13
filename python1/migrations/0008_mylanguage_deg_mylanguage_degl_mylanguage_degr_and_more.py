# Generated by Django 4.0 on 2022-02-25 19:12

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python1', '0007_myknowledge_mylanguage_myskills'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylanguage',
            name='deg',
            field=computed_property.fields.ComputedDecimalField(compute_from='degdef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
        migrations.AddField(
            model_name='mylanguage',
            name='degl',
            field=computed_property.fields.ComputedDecimalField(compute_from='degldef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
        migrations.AddField(
            model_name='mylanguage',
            name='degr',
            field=computed_property.fields.ComputedDecimalField(compute_from='degrdef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
        migrations.AddField(
            model_name='myskills',
            name='deg',
            field=computed_property.fields.ComputedDecimalField(compute_from='degdef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
        migrations.AddField(
            model_name='myskills',
            name='degl',
            field=computed_property.fields.ComputedDecimalField(compute_from='degldef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
        migrations.AddField(
            model_name='myskills',
            name='degr',
            field=computed_property.fields.ComputedDecimalField(compute_from='degrdef', decimal_places=2, default='0', editable=False, max_digits=100),
        ),
    ]