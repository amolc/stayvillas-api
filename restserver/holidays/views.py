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
        # print(f"Received org_id: {request_data}")
        request_data['org_id'] = org_id
        
        # Handle image uploads
        # Handle base64 image uploads

        print(request_data['holiday_image1'])
        print(request_data['holiday_image2'])


        
        if 'holiday_image1' in request_data and request_data['holiday_image1']:
            try:
                base64_image = self.get_image_from_url_as_base64(request_data['holiday_image1'])
                # Print only the first 50 characters of the base64 string to avoid log flooding
                if base64_image:
                    truncated_base64 = base64_image[:50] + "..." if len(base64_image) > 50 else base64_image
                    print(f"Base64 image (truncated): {truncated_base64}")
                else:
                    print("Base64 image: None")
                if base64_image:  # Add this check to ensure base64_image is not None
                    image1_path = self.save_base64_image(base64_image, 'holidays')
                    request_data['holiday_image1'] = image1_path
                    print(f"Processed holiday_image1: {image1_path}")
                else:
                    print("Failed to convert image URL to base64")
            except Exception as e:
                print(f"Error processing holiday_image1: {str(e)}")
            
        if 'holiday_image2' in request_data and request_data['holiday_image2']:
            try:
                base64_image = self.get_image_from_url_as_base64(request_data['holiday_image2'])
                print(f"Base64 image: {base64_image}")
                image2_path = self.save_base64_image(base64_image, 'holidays')
                request_data['holiday_image2'] = image2_path
                print(f"Processed holiday_image2: {image2_path}")
            except Exception as e:
                print(f"Error processing holiday_image2: {str(e)}")
        
        serializer = HolidaySerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def save_image(self, image, folder):
        import os
        from django.conf import settings
        import uuid
        
        # Create a unique filename to avoid overwriting
        filename = f"{uuid.uuid4()}_{image.name}"
        print(f"Generated filename: {filename}")
        
        # Ensure the directory exists
        upload_dir = os.path.join(settings.STATIC_ROOT, folder)
        print(f"Upload directory: {upload_dir}")
        print(f"Directory exists: {os.path.exists(upload_dir)}")
        # Remove the breakpoint line
        if not os.path.exists(upload_dir):
            print(f"Creating directory: {upload_dir}")
            os.makedirs(upload_dir)
        else:
            print(f"Directory already exists: {upload_dir}")
            
        # Save the file
        file_path = os.path.join(upload_dir, filename)
        print(f"Saving file to: {file_path}")
        with open(file_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        print(f"File saved successfully: {file_path}")
                
        # Return the relative path for storage in the database
        return_path = f"/static/{folder}/{filename}"
        print(f"Returning path for database: {return_path}")
        return return_path

    def get(self, request, id=None, org_id=None):
        if id:
            try:
                holiday = get_object_or_404(Holiday, id=id)
                serializer = HolidaySerializer(holiday)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"status": "error", "message": f"Invalid ID format: {id}"}, 
                               status=status.HTTP_400_BAD_REQUEST)

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

    def save_base64_image(self, base64_data, folder):
        import os
        import base64
        import uuid
        from django.conf import settings
        
        # Extract the actual base64 data if it includes the data URI scheme
        if ',' in base64_data:
            format, base64_data = base64_data.split(';base64,')
            ext = format.split('/')[-1]
        else:
            # Default to png if format is not specified
            ext = 'png'
        
        # Create a unique filename
        filename = f"{uuid.uuid4()}.{ext}"
        print(f"Generated filename for base64 image: {filename}")
        
        # Ensure the directory exists - use a fallback if STATIC_ROOT is not set
        if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
            upload_dir = os.path.join(settings.STATIC_ROOT, folder)
        else:
            # Fallback to a directory in the project
            base_dir = getattr(settings, 'BASE_DIR', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            upload_dir = os.path.join(base_dir, 'static', folder)
            
        print(f"Upload directory: {upload_dir}")
        print(f"Directory exists: {os.path.exists(upload_dir)}")
        
        # Remove the breakpoint
        if not os.path.exists(upload_dir):
            print(f"Creating directory: {upload_dir}")
            os.makedirs(upload_dir, exist_ok=True)
        else:
            print(f"Directory already exists: {upload_dir}")
        
        # Save the file
        file_path = os.path.join(upload_dir, filename)
        print(f"Saving base64 image to: {file_path}")
        
        try:
            # Decode the base64 data and write to file
            image_data = base64.b64decode(base64_data)
            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            print(f"Base64 image saved successfully: {file_path}")
            
            # Return the relative path for storage in the database
            return_path = f"/static/{folder}/{filename}"
            print(f"Returning path for database: {return_path}")
            return return_path
        except Exception as e:
            print(f"Error saving base64 image: {str(e)}")
            raise e

    def get_image_from_url_as_base64(self, url):
        """
        Fetches an image from a URL and converts it to base64 encoding
        """
        import requests
        import base64
        from io import BytesIO
        
        try:
            # Fetch the image from the URL
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Get the content type from headers
            content_type = response.headers.get('Content-Type', 'image/jpeg')
            
            # Read the image data
            image_data = BytesIO(response.content).read()
            
            # Encode to base64
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
            
            # Return with data URI scheme
            return f"data:{content_type};base64,{base64_encoded}"
            
        except Exception as e:
            print(f"Error fetching image from URL: {str(e)}")
            return None
