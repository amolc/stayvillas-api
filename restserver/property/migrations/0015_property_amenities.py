# Generated by Django 5.1 on 2024-10-16 04:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_merge_20241010_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='amenities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
    ]