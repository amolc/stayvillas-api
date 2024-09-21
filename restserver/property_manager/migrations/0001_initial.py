# Generated by Django 5.1 on 2024-09-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.PositiveIntegerField(blank=True, null=True)),
                ('manager_name', models.CharField(max_length=255)),
                ('manager_email', models.EmailField(max_length=254, unique=True)),
                ('manager_phone', models.CharField(max_length=20)),
                ('availability_status', models.BooleanField(default=True)),
                ('date_of_hire', models.DateTimeField()),
                ('total_properties_managed', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
