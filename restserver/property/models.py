from django.db import models

# Create your models here.

class Property(models.Model):
    org_id = models.PositiveIntegerField()
    property_name = models.CharField(max_length=200)
    property_key_name = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.IntegerField(default=0)


    class Meta:
        db_table = "Property"

        def __str__(self):
            return self.property_name