import os

from .base import *  # type: ignore # noqa: F403 F401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('MYSQL_DB', 'stayvillas'),
        'USER': os.environ.get('MYSQL_USER', 'stockrobot'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', '10gXWOqeaf'),
        'HOST': os.environ.get('MYSQL_HOST', 'api.stayvillas.co'),
        'PORT': os.environ.get('MYSQL_PORT', '5432'),  # Default MySQL port
    }
}
