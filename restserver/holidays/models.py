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
    accommodation_property_id_1 = models.PositiveIntegerField(blank=True, null=True)
    accommodation_property_id_2 = models.PositiveIntegerField(blank=True, null=True)
    accommodation_property_id_3 = models.PositiveIntegerField(blank=True, null=True)
    holiday_inclusion = models.TextField(blank=True, null=True)
    day_wise_itinerary = models.TextField(blank=True, null=True)
    terms_and_condition = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
