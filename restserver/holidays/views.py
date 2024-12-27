from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Holiday
from .serializers import HolidaySerializer

class HolidayViews(APIView):

    def post(self, request, org_id=None):
        # Add org_id to the request data if needed
        request_data = request.data.copy()
        request_data['org_id'] = org_id  

        serializer = HolidaySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            
            holiday = get_object_or_404(Holiday, id=id)  # Corrected to use 'eventdata'
            serializer = HolidaySerializer(holiday)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Fetch all events if no ID is provided
        holidays = Holiday.objects.all()
        serializer = HolidaySerializer(holidays, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        if not id:
            return Response({'status': 'error', 'message': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        holiday = get_object_or_404(Holiday, id=id)  # Corrected to use 'eventdata'
        serializer = HolidaySerializer(holiday, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        try:
            holiday = get_object_or_404(Holiday, id=id)
            holiday.delete()
            return Response({"status": "success", "message": "Holiday deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
