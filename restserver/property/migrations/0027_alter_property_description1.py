# Generated by Django 5.1 on 2024-11-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_alter_property_description1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description1',
            field=models.TextField(default=''),
        ),
    ]
