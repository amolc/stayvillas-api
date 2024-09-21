# Generated by Django 5.1.1 on 2024-09-21 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.PositiveIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=15)),
                ('property_location', models.CharField(max_length=255)),
                ('property_type', models.CharField(choices=[('Villa', 'Villa'), ('Cottage', 'Cottage'), ('Bungalow', 'Bungalow'), ('Under Construction', 'Under Construction')], max_length=50)),
                ('num_rooms', models.PositiveIntegerField()),
                ('heard_from', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Google Search', 'Google Search'), ('Reference from Guest', 'Reference from Guest'), ('Reference from Property Owner', 'Reference from Property Owner'), ('Blogs', 'Blogs')], max_length=50)),
                ('photo_website', models.URLField(blank=True, null=True)),
                ('property_description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'property_listings',
            },
        ),
    ]
