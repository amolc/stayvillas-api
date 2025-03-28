# Generated by Django 5.1 on 2025-03-19 07:45

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.PositiveIntegerField()),
                ('property_name', models.CharField(max_length=100)),
                ('property_key_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('cost_per_night', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('title', models.CharField(default='Add Title', max_length=255)),
                ('property_type', models.CharField(choices=[('Villa', 'Villa'), ('Bungalow', 'Bungalow'), ('Hotel', 'Hotel')], default='Select Property Type', max_length=50)),
                ('price_villa', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_room', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('num_rooms', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(default='No description available')),
                ('floors', models.PositiveIntegerField(default=0)),
                ('num_bedrooms', models.PositiveIntegerField(default=0)),
                ('num_bathrooms', models.PositiveIntegerField(default=0)),
                ('guest_limit', models.PositiveIntegerField(default=0)),
                ('meals_available', models.TextField(blank=True, null=True)),
                ('bedroom1_image', models.TextField(blank=True, null=True)),
                ('description1', models.TextField(default='')),
                ('bedroom2_image', models.TextField(blank=True, null=True)),
                ('description2', models.TextField(default='')),
                ('bedroom3_image', models.TextField(blank=True, null=True)),
                ('description3', models.TextField(default='')),
                ('bedroom4_image', models.TextField(blank=True, null=True)),
                ('description4', models.TextField(default='')),
                ('total_bedroom_size', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('square_feet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('location_url', models.TextField(blank=True, null=True)),
                ('video_url', models.TextField(blank=True, null=True)),
                ('great_for', models.CharField(choices=[('Senior_Citizen', 'Senior_Citizen'), ('Kids', 'Kids'), ('Adults', 'Adults'), ('All', 'All'), ('Others', 'Others')], default='all', max_length=50)),
                ('other_images', models.TextField(blank=True, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('img3', models.TextField(blank=True, null=True)),
                ('address1', models.CharField(default='Unknown', max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(default='Enter Pincode', max_length=20)),
                ('amenities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None)),
                ('best_rated', models.BooleanField(default=False)),
                ('most_loved', models.BooleanField(default=False)),
                ('agent_id', models.PositiveIntegerField(default=1)),
                ('room_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('room_name_1_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('room_name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('room_name_2_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('room_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('room_name_3_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('room_name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('room_name_4_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(default=0)),
                ('updated_date', models.DateTimeField(null=True)),
                ('updated_by', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Property',
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property/image')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='propertyImage', to='property.property')),
            ],
        ),
    ]
