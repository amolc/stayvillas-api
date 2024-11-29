# Generated by Django 5.1 on 2024-11-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='reset_password_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='reset_password_token',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]