# Generated by Django 5.1.1 on 2024-10-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_customer_remove_booking_customer_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customers',
            field=models.ManyToManyField(to='booking.customer'),
        ),
    ]