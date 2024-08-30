# drf
from django.db import transaction
from django.core.files.base import ContentFile
import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# custom
from .serializers import PropertySerializer
from .models import Property, PropertyImages
from common.utils import StayVillasResponse


class PropertyViews(APIView):

    def post(self, request, org_id=None):

        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id
            serializer = PropertySerializer(data=request_data)
            if serializer.is_valid():
                
                with transaction.atomic():
                    serializer.save()

                    property_id = serializer.data.get('id')
                    property_name = serializer.data.get('property_name')
                    property_key_name = property_name.lower().replace(" ", "_")
                    print(property_key_name)

                    # property_images = request_data.pop('propertyImages', [])
                    # for idx, image_data_encoded in enumerate(property_images):
                    #     format, imgstr = image_data_encoded.split(';base64,')  
                    #     ext = format.split('/')[-1]  
                    #     image_file = ContentFile(base64.b64decode(imgstr), name=f'{property_key_name}_{idx}.{ext}')  
                    #     print("-----------image_file-----------", image_file)
                    #     PropertyImages.objects.create(property_id_id=property_id, image=image_file)


                    return Response(
                        {"status": "success", "data": serializer.data},
                        status=status.HTTP_200_OK,
                    )
            else:
                return StayVillasResponse.serializer_error(self.__class__.__name__, request, serializer)
        
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def get(self, request, id=None, org_id=None):
        try:
            property_id = request.query_params.get('property_id')
            if property_id:
                item = Property.objects.get(id=property_id)
                serializer = PropertySerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )

            items = Property.objects.all()
            serializer = PropertySerializer(items, many=True)
            return Response(
                {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def put(self, request, id=None, org_id=None):

        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id
            property_id = request.query_params.get('property_id')
            item = Property.objects.get(id=property_id)
            serializer = PropertySerializer(item, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return StayVillasResponse.serializer_error(self.__class__.__name__, request, serializer)
        
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)
        
    def delete(self, request, id=None, org_id=None):
        
        try:
            property_id = request.query_params.get('property_id')
            Property.objects.get(id=property_id).delete()
            return Response({"status": "success", "data": "Property Deleted"})
        
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

