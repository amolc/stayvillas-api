# Generated by Django 5.1 on 2024-11-25 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0003_enquiry_num_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='num_rooms',
            new_name='num_guests',
        ),
    ]