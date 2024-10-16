# Generated by Django 5.1 on 2024-10-16 05:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_property_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), blank=True, default=list, size=None),
        ),
    ]
