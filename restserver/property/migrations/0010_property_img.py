# Generated by Django 5.1.1 on 2024-10-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_property_bedroom1_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='img',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]