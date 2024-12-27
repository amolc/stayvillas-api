from .base import *  # type: ignore # noqa: F403 F401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stayvillas_dev',
        'USER': 'stayvillas_dev',
        'PASSWORD': '!Xdasdf890',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
