import traceback

# drf
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# custom
from .serializers import PropertySerializer
from .models import Property


class PropertyViews(APIView):

    def post(self, request, org_id=None):

        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id
            serializer = PropertySerializer(data=request_data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
            {"status": "error", "data": str(e), "traceback": traceback.format_exc()},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

    def get(self, request, id=None, org_id=None):
        try:
            if id:
                item = Property.objects.get(id=id)
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
            return Response(
            {"status": "error", "data": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

    def put(self, request, id=None, org_id=None):

        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id
            print(id)

            item = Property.objects.get(id=id)
            serializer = PropertySerializer(item, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        
        except Exception as e:
            return Response(
            {"status": "error", "data": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
    def delete(self, request, id=None, org_id=None):
        
        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id
            Property.objects.get(id=id).delete()
            return Response({"status": "success", "data": "Item Deleted"})
        
        except Exception as e:
            return Response(
            {"status": "error", "data": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

