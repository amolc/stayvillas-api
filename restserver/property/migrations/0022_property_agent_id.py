# Generated by Django 5.1 on 2024-10-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_remove_property_agent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='agent_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
