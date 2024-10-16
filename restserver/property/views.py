from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import urlparse
import re
from .models import Property, PropertyImages
from .serializers import PropertyImageSerializer, PropertySerializer

class PropertyViews(APIView):
    def get(self, request, id=None, org_id=None):
        if id:
            # Fetch a single property by its ID
            property_item = get_object_or_404(Property, id=id)
            serializer = PropertySerializer(property_item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch all properties, filtered by org_id if provided
        properties = Property.objects.filter(org_id=org_id) if org_id else Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data["org_id"] = org_id
        print("Received data:", request_data)

        serializer = PropertySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        print("Serializer errors:", serializer.errors)  # Debug line
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'Property ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        request_data["org_id"] = org_id

        property_item = get_object_or_404(Property, id=id)

        serializer = PropertySerializer(property_item, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'Property ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        property_item = get_object_or_404(Property, id=id)
        property_item.delete()
        return Response({'status': 'success', 'message': 'Property deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class PropertyImageViews(APIView):
    def post(self, request, org_id=None, property_id=None):
        if not org_id:
            return Response({'status': 'error', 'message': 'Organization ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not property_id:
            return Response({'status': 'error', 'message': 'Property ID is required to upload images'}, status=status.HTTP_400_BAD_REQUEST)
         
        property_obj = get_object_or_404(Property, id=property_id, org_id=org_id)

        request_data = request.data.copy()
        request_data["property_id"] = property_id
        
        serializer = PropertyImageSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, org_id=None, image_id=None):
        if not org_id:
            return Response({'status': 'error', 'message': 'Organization ID is required'}, status=status.HTTP_400_BAD_REQUEST)
         
        if not image_id:
            return Response({'status': 'error', 'message': 'Image ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)
        
        image_item = get_object_or_404(PropertyImages, id=image_id)
        image_item.delete()
        return Response({'status': 'success', 'message': 'Image deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
class PropertySearchViews(APIView):
    def post(self, request, id=None, org_id=None):
        data = request.data

        # Get the city filter from request data
        cities = data.get('city', None)

        # Initialize the queryset
        properties = Property.objects.all()

        # Apply city filter if provided
        if cities:
            if isinstance(cities, list):
                properties = properties.filter(city__in=cities)  # Filter by multiple cities
            else:
                properties = properties.filter(city__iexact=cities)  # Filter by a single city
        
        # Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)