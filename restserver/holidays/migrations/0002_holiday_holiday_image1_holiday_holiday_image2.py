# Generated by Django 5.1 on 2024-12-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='holiday_image1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='holiday',
            name='holiday_image2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]