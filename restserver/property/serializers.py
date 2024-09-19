# django
from rest_framework import serializers

# custom
from .models import Property, PropertyImages


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': True}  # Ensures the image field is required
        }