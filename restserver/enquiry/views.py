from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer
from django.shortcuts import get_object_or_404
from .utils import send_booking_enquiry_mail  # Import the utility function

class EnquiryViews(APIView):
    def post(self, request, org_id=None):
        request_data = request.data.copy()
        request_data['org_id'] = org_id

        serializer = EnquirySerializer(data=request_data)
        if serializer.is_valid():
            enquiry = serializer.save()  # Save enquiry data in the database

            # Send email
            try:
                email = enquiry.email  # Get email from the saved instance
                if email:
                    subject = "Booking Enquiry Received"
                    body_text = f"""
                    Hello {enquiry.first_name or 'Guest'}, 

                    Thank you for your enquiry. Our team will contact you soon.
                    """
                    body_html = f"""
                    <html>
                    <head></head>
                    <body>
                        <h1>Thank You for Your Enquiry!</h1>
                        <p>Hello {enquiry.first_name or 'Guest'},</p>
                        <p>We have received your enquiry with the following details:</p>
                        <ul>
                            <li>PropertyId: {enquiry.propertyId or 'N/A'}</li>
                            <li>agnetId: {enquiry.agentId or 'N/A'}</li>
                            <li>Number of Guests: {enquiry.num_guests or 'N/A'}</li>
                        </ul>
                        <p>Our team will contact you soon.</p>
                    </body>
                    </html>
                    """
                    send_booking_enquiry_mail(
                        recipient=email,
                        subject=subject,
                        body_text=body_text,
                        body_html=body_html
                    )
                    print(f"Enquiry email sent to {email}.")
                else:
                    print("No email provided for enquiry.")
            except Exception as e:
                print(f"Error sending enquiry email: {str(e)}")  # Log the error for debugging

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            enquiry = get_object_or_404(Enquiry, id=id)
            serializer = EnquirySerializer(enquiry)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        enquiries = Enquiry.objects.all()
        serializer = EnquirySerializer(enquiries, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        enquiry = get_object_or_404(Enquiry, id=id)
        serializer = EnquirySerializer(enquiry, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, org_id=None):
        enquiry = get_object_or_404(Enquiry, id=id)
        enquiry.delete()
        return Response({"status": "success", "message": "Enquiry deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
