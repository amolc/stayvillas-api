# Generated by Django 5.1.1 on 2024-10-19 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_rename_mobile_no_customer_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Guest',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customers',
            new_name='guests',
        ),
    ]