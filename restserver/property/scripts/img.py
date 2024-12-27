from PIL import Image
import os
from django.conf import settings

def run():
    base_width = 300
    
    img_path = os.path.join(settings.MEDIA_ROOT, 'property/image/villa-amethyst.jpg')
    img = Image.open(img_path)
    
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    
    save_dir = os.path.join(settings.MEDIA_ROOT, 'save')
    os.makedirs(save_dir, exist_ok=True)  
    
    save_path = os.path.join(save_dir, 'villa-amethyst-resized.jpg')
    img.save(save_path)
