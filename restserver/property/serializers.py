# django
from rest_framework import serializers

# custom
from .models import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = "__all__"