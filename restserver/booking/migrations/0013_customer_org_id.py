# Generated by Django 5.1.1 on 2024-10-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_rename_guest_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='org_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
