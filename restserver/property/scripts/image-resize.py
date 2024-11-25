from PIL import Image


import os
from pathlib import Path
# import environ

# Initialize environment variables
# env = environ.Env()

# Take environment variables from .env file
# environ.Env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # type: ignore

somepic = os.path.join(MEDIA_ROOT, 'somepic.jpg')



base_width = 300
img = Image.open(somepic)
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
img.save(newpic.png, 'JPEG')


img2 = Image.open(newpic)
img2buffer = img2.tobytes()
