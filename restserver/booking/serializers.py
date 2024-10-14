from rest_framework import serializers
from .models import Booking, EventBooking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = '__all__'