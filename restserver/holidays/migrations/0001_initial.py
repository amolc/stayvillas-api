# Generated by Django 5.1 on 2024-12-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('num_of_days', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('operated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('meals_short_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('max_group_size', models.PositiveIntegerField()),
                ('highlights', models.TextField(blank=True, null=True)),
                ('meals', models.TextField(blank=True, null=True)),
                ('flights', models.TextField(blank=True, null=True)),
                ('accommodation_property_id_1', models.PositiveIntegerField(blank=True, null=True)),
                ('accommodation_property_id_2', models.PositiveIntegerField(blank=True, null=True)),
                ('accommodation_property_id_3', models.PositiveIntegerField(blank=True, null=True)),
                ('holiday_inclusion', models.TextField(blank=True, null=True)),
                ('day_wise_itinerary', models.TextField(blank=True, null=True)),
                ('terms_and_condition', models.TextField(blank=True, null=True)),
            ],
        ),
    ]