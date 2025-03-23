# Create your models here.
from django.db import models


class Holiday(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, blank=True, null=True)
    num_of_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    operated_by = models.CharField(max_length=255, blank=True, null=True)
    meals_short_tag = models.CharField(max_length=255, blank=True, null=True)
    max_group_size = models.PositiveIntegerField()
    highlights = models.TextField(blank=True, null=True)
    meals = models.TextField(blank=True, null=True)
    flights = models.TextField(blank=True, null=True)
    accommodation_property_id_1 = models.TextField(blank=True, null=True)
    accommodation_property_id_2 = models.TextField(blank=True, null=True)
    accommodation_property_id_3 = models.TextField(blank=True, null=True)
    holiday_inclusion = models.TextField(blank=True, null=True)
    day_wise_itinerary = models.TextField(blank=True, null=True)
    terms_and_condition = models.TextField(blank=True, null=True)
    holiday_image1 = models.TextField( null=True, blank=True)  # First product image path
    holiday_image2 = models.TextField( null=True, blank=True)  # First product image path
    cities = models.TextField( null=True, blank=True)  # First product image path
    keywords = models.TextField( null=True, blank=True)  # First product image path
    meta_title = models.TextField( null=True, blank=True)  # First product image path
    meta_keywords = models.TextField( null=True, blank=True)  # First product image path
    meta_description = models.TextField( null=True, blank=True)  # First product image path

    def __str__(self):
        return self.title
