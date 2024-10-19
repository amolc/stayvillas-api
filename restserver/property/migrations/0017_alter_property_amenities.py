# Generated by Django 5.1 on 2024-10-16 09:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_alter_property_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
    ]