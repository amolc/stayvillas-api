# Generated by Django 5.1 on 2024-11-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_alter_property_great_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description1',
            field=models.TextField(blank=True, null=True),
        ),
    ]
