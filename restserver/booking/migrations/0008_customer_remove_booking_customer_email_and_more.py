# Generated by Django 5.1.1 on 2024-10-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_booking_customer_email_booking_customer_mobile_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_mobile_no',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_name',
        ),
    ]
