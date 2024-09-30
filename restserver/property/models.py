from django.db import models

# Create your models here.
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Villa', 'Villa'),
        ('Bungalow', 'Bungalow'),
        ('Hotel', 'Hotel'),
    ]
    
    GREAT_FOR_CHOICES = [
        ('senior_citizen', 'Senior Citizen'),
        ('kids', 'Kids'),
        ('adults', 'Adults'),
        ('all', 'All of the Above'),
         ('Others', 'others'),
    ]

    org_id = models.PositiveIntegerField()
    property_name = models.CharField(max_length=100)
    property_key_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=50)  # Increased length
    state = models.CharField(max_length=50)  # Increased length
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # New fields
    title = models.CharField(max_length=255, default='Add Title')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES, default='Select Property Type')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(default='No description available')
    floors = models.PositiveIntegerField(default=0)
    num_bedrooms = models.PositiveIntegerField(default=0)
    num_bathrooms = models.PositiveIntegerField(default=0)
    guest_limit = models.PositiveIntegerField(default=0)
    meals_available = models.TextField(null=True, blank=True)
    
    # Bedroom image URLs
    bedroom1_image = models.URLField(null=True, blank=True)
    bedroom2_image = models.URLField(null=True, blank=True)
    bedroom3_image = models.URLField(null=True, blank=True)
    bedroom4_image = models.URLField(null=True, blank=True)

    total_bedroom_size = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    square_feet = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    location_url = models.URLField(null=True, blank=True)
    great_for = models.CharField(max_length=50, choices=GREAT_FOR_CHOICES, default='all')
    other_images = models.URLField(null=True, blank=True)
    address1 = models.CharField(max_length=100, default='Unknown')
    address2 = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=20, default='Enter Pincode')
    
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    updated_date = models.DateTimeField(null=True)
    updated_by = models.IntegerField(default=0)

    class Meta:
        db_table = "Property"

    def __str__(self):
        return self.property_name
        

class PropertyImages(models.Model):
    property_id = models.ForeignKey('Property', on_delete=models.RESTRICT, related_name='propertyImage',)
    image = models.ImageField(upload_to='property/image')
    
    def __str__(self):
        return f"Image for Property ID {self.property_id.id}"