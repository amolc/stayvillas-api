# views.py
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DestinationSerializer
from .models import Destination
from common.utils import StayVillasResponse

class DestinationViews(APIView):

    def get(self, request, id=None):
        try:
            if id:
                item = Destination.objects.get(id=id)
                serializer = DestinationSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                items = Destination.objects.all()
                serializer = DestinationSerializer(items, many=True)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
        except Destination.DoesNotExist:
            return Response({'status': 'error', 'message': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def post(self, request):
        try:
            serializer = DestinationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def put(self, request, id=None):
        try:
            if not id:
                return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)
            
            item = Destination.objects.get(id=id)
            serializer = DestinationSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Destination.DoesNotExist:
            return Response({'status': 'error', 'message': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)

    def delete(self, request, id=None):
        try:
            if not id:
                return Response({'status': 'error', 'message': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

            item = Destination.objects.get(id=id)
            item.delete()
            return Response({'status': 'success', 'message': 'Destination deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Destination.DoesNotExist:
            return Response({'status': 'error', 'message': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return StayVillasResponse.exception_error(self.__class__.__name__, request, e)
