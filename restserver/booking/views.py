from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import get_object_or_404

class BookingViews(APIView):
    
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data['org_id'] = org_id

        serializer = BookingSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            booking = get_object_or_404(Booking, id=id)
            serializer = BookingSerializer(booking)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        bookings = Booking.objects.filter(org_id=org_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        booking = get_object_or_404(Booking, id=id)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        booking = get_object_or_404(Booking, id=id)
        booking.delete()
        return Response({"status": "success", "message": "Booking deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
