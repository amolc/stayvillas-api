from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.CharField(max_length=15,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)

    def __str__(self):
        return self.name
class Booking(models.Model):
    org_id = models.PositiveIntegerField(null=True, blank=True)

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    propertyId = models.PositiveIntegerField(default=0, null=True, blank=True)
    agentId = models.PositiveIntegerField(default=0, null=True, blank=True)
    num_guests = models.IntegerField(default=1)
    num_rooms = models.IntegerField(default=1)  # Add number of rooms
    # special_requests = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   
    customers = models.ManyToManyField(Customer)

    def __str__(self):
        return f"{self.guest_name} - {self.property_type} Booking"
class EventBooking(models.Model):
    org_id = models.PositiveIntegerField(null=True, blank=True)
   
    # Customer details
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(default='default@example.com')
    customer_mobile_no = models.CharField(max_length=15)

    gst = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return f"Booking for {self.event.title} by {self.customer_name}"