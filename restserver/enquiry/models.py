from django.db import models

# Create your models here.
class Enquiry(models.Model):
    NEW_BOOKING = 'New Booking'
    EXISTING_BOOKING = 'Existing Booking'
    UPCOMING_BOOKING = 'Upcoming Booking'

    CONCERN_CHOICES = [
        (NEW_BOOKING, 'New Booking'),
        (EXISTING_BOOKING, 'Existing Booking'),
        (UPCOMING_BOOKING, 'Upcoming Booking'),
    ]

    org_id = models.PositiveIntegerField(null=True, blank=True)  # Organization ID
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, default='', null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    num_guests = models.PositiveIntegerField(default=0, null=True, blank=True)
    propertyId = models.PositiveIntegerField(default=0, null=True, blank=True)
    agentId = models.PositiveIntegerField(default=0, null=True, blank=True)
    concern = models.CharField(max_length=50, choices=CONCERN_CHOICES, null=True, blank=True)
    property_location = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "enquiries"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.concern}"
