# Generated by Django 5.1 on 2024-11-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
