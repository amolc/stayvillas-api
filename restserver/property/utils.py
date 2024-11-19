import base64
from io import BytesIO
from PIL import Image

def resize_base64_image(base64_image, width):
    try:
        image_data = base64.b64decode(base64_image)
        img = Image.open(BytesIO(image_data))

        wpercent = (width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((width, hsize), Image.Resampling.LANCZOS)

        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)
        resized_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return resized_base64
    except Exception as e:
        print(f"Error resizing image: {e}")
        return base64_image
