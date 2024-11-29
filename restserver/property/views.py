from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib.parse import urlparse
import re
from .models import Property, PropertyImages
from .serializers import PropertyImageSerializer, PropertySerializer
from .utils import resize_base64_image

import icecream as ic

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
            print(request_data)
            # Handle the image resize here
            if 'other_images' in request_data:
                original_image = request_data['other_images']
                print(original_image)
                # breakpoint()
                resized_image = resize_base64_image(original_image, base_width=300) 
                print(resized_image)
                request_data['other_images'] = resized_image

            serializer = PropertySerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
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



class EditPropertyViews(APIView):

    def patch(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'Property ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        request_data["org_id"] = org_id
        # print(id)
        PropertyInstance = Property.objects.get(id=id)
        # print(PropertyInstance)

        # Let's resize the image.
        if 'other_images' in request_data:
            original_image = request_data['other_images']
            # print(original_image)
            # breakpoint()
            resized_image = resize_base64_image(original_image, base_height=300) 
            print(resized_image)
            request_data['other_images'] = resized_image
            
        serializer = PropertySerializer(PropertyInstance, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response({"status": "success", "data": request.data}, status=status.HTTP_400_BAD_REQUEST)



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
class PropertyFilterViews(APIView):
    def post(self, request, id=None, org_id=None):
        data = request.data

        # Debug log to check the received data
        print("Received filter data:", data)

        # Get price range filter from request data
        price_filter = data.get('price', {})
        min_price = price_filter.get('min', None)
        max_price = price_filter.get('max', None)

        # Debug log to check the price filter values
        print(f"Min price: {min_price}, Max price: {max_price}")

        # Initialize the queryset
        properties = Property.objects.all()

        # Apply price range filter if provided
        if min_price is not None:
            properties = properties.filter(cost_per_night__gte=min_price)
        if max_price is not None:
            properties = properties.filter(cost_per_night__lte=max_price)

        # Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class PropertyTopFilterViews(APIView):
     def post(self, request, id=None, org_id=None):
        data = request.data

        # Extract filter values from the request
        best_rated = data.get('best_rated', None)
        most_loved = data.get('most_loved', None)

        # Initialize the queryset with all properties
        properties = Property.objects.all()

        # Apply filter logic based on the selected filters
        if best_rated is not None and most_loved is not None:
            # Apply AND condition (both filters are true)
            properties = properties.filter(best_rated=best_rated, most_loved=most_loved)
        elif best_rated is not None or most_loved is not None:
            # Apply OR condition (either one or both are selected)
            conditions = Q()  # Initialize an empty Q object
            if best_rated is not None:
                conditions |= Q(best_rated=best_rated)  # Add OR condition for best_rated
            if most_loved is not None:
                conditions |= Q(most_loved=most_loved)  # Add OR condition for most_loved
            properties = properties.filter(conditions)

        # Serialize and return the filtered properties
        serializer = PropertySerializer(properties, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
class PropertySortViews(APIView):
    def post(self, request, id=None, org_id=None):
        data = request.data

        # Get the sort option from request data
        sort_by = data.get('sort_by', None)

        # Initialize the queryset
        properties = Property.objects.all()

        # Apply sorting based on the sort_by parameter
        if sort_by == 'most_loved':
            properties = properties.order_by('-most_loved')
        elif sort_by == 'price':
            properties = properties.order_by('cost_per_night')
        elif sort_by == 'best_rated':
            properties = properties.order_by('-best_rated')
        
        # Serialize the sorted properties
        serializer = PropertySerializer(properties, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
class PropertyAgentViews(APIView):
    def post(self, request, id=None, org_id=None):
        print("Request received at property agent filter view")  # Debugging line
        data = request.data
        print("Data received:", data)  # Debugging line

        # Get the agent_id from request data
        agent_id = data.get('agent_id', None)
        print("Agent ID:", agent_id)  # Debugging line

        if agent_id is None:
            return Response({'status': 'error', 'message': 'agent_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Initialize the queryset
        properties = Property.objects.all()

        # Apply agent_id filter if provided
        properties = properties.filter(agent_id=agent_id)

        # Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        # Return the serialized data
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class PropertyAgentPropertiesViews(APIView):
    def get(self, request, agent_id=None, org_id=None):
        print("Request received at property agent filter view")  # Debugging line

        # Use 'agent_id' from the URL path
        print("Agent ID:", agent_id)  # Debugging line

        if agent_id is None:
            return Response({'status': 'error', 'message': 'agent_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter properties based on the agent_id
        properties = Property.objects.filter(agent_id=agent_id)

        # Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        # Return the serialized data
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class PropertyFilterByViews(APIView):
    def get(self, request, id=None, org_id=None):
        print("Request received at property agent filter view")  # Debugging line
        data = request.query_params
        print("Query params received:", data)  # Debugging line

        # Initialize the queryset with all properties
        properties = Property.objects.all()

        # Handle 'type' filter (if present in query params)
        property_type = data.get('type', None)
        if property_type:
            if property_type in dict(Property.PROPERTY_TYPE_CHOICES):
                properties = properties.filter(property_type=property_type)
            else:
                return Response({'status': 'error', 'message': 'Invalid property type'}, status=status.HTTP_400_BAD_REQUEST)

        # Handle 'city' filter (if present in query params)
        city = data.get('city', None)
        if city:
            properties = properties.filter(city=city)

        # Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        # Return the serialized data
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

class PropertyAgentPropertyViews(APIView):
    def get(self, request, agent_id=None, org_id=None):
        print("Request received at property agent filter view")  # Debugging line

        # Use 'agent_id' from the URL path
        print("Agent ID:", agent_id)  # Debugging line

        if agent_id is None:
            return Response({'status': 'error', 'message': 'agent_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Retrieve properties based on the agent_id
        properties = Property.objects.filter(agent_id=agent_id)

        # Get the query parameters from the request
        data = request.query_params

        # Step 2: Handle 'property_type' filter (if present in query params)
        property_type = data.get('type', None)
        if property_type:
            # Validate if the provided 'property_type' is a valid choice
            if property_type in dict(Property.PROPERTY_TYPE_CHOICES):
                properties = properties.filter(property_type=property_type)
            else:
                return Response({'status': 'error', 'message': 'Invalid property type'}, status=status.HTTP_400_BAD_REQUEST)

        # Step 3: Handle 'city' filter (if present in query params)
        city = data.get('city', None)
        if city:
            properties = properties.filter(city=city)

        # Step 4: Serialize the filtered properties
        serializer = PropertySerializer(properties, many=True)

        # Return the serialized data as a response
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

