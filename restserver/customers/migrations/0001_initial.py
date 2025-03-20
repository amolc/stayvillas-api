# Generated by Django 5.1 on 2025-03-19 07:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('org_id', models.PositiveIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('logid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('transaction_name', models.CharField(max_length=500)),
                ('mode', models.CharField(max_length=100)),
                ('log_message', models.TextField()),
                ('is_app', models.BooleanField(default=False)),
                ('log_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='log_Customer_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Logs',
            },
        ),
    ]
