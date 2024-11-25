import base64
from io import BytesIO
from PIL import Image
from django.conf import settings
import os

# import base64
# from PIL import Image
# from io import BytesIO

def resize_base64_image(base64_image, base_height=300):
    try:
        # Split the Base64 string to get the data part (after the comma)
        parts = base64_image.split(",", 1)
        mime_type = parts[0]  # MIME type (e.g., "data:image/jpeg;base64")
        base64_data = parts[1]  # The Base64 encoded image data

        # Decode the Base64 string into binary image data
        img = base64.b64decode(base64_data)

        # Open the image from the binary data
        newimage = Image.open(BytesIO(img))
        print("Original Image Size:", newimage.size)
        print("Image Format:", newimage.format)
        print("Image Mode:", newimage.mode)

        # Calculate new width based on the given base height
        wpercent = (base_height / float(newimage.size[1]))  # Ratio of new height to original height
        new_width = int((float(newimage.size[0]) * float(wpercent)))  # Calculate new width
        print("New Width:", new_width)

        # Resize the image
        try:
            newimage = newimage.resize((new_width, base_height), Image.Resampling.LANCZOS)
        except Exception as e:
            print(f"Error resizing image: {e}")
        # newimage = newimage.resize((new_width, base_height), Image.Resampling.LANCZOS)
        print("Resized Image Size:", newimage)

       
        


        # Save the resized image into a BytesIO buffer
        buffered = BytesIO()
        newimage.save(buffered, format="JPEG")
        buffered.seek(0)

        # Convert the image in the buffer back to Base64
        resized_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        base64_image = "data:image/jpeg;base64,"+resized_base64

        media_root = settings.MEDIA_ROOT
        file_path = os.path.join(media_root, "resized_img.jpg")
        with open(file_path, "wb") as image_file:
            image_file.write(buffered.getvalue())
        
        return base64_image
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None

