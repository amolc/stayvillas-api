from django.db import models

class Destination(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.TextField(null=True, blank=True)
    order_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Destination'
