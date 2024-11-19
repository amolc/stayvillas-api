"""
Django settings for restserver project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
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
# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kd$!n!^n!zu-cp3c6he_9)+q!vd@z-06yb*fm9^9jvdoz80=)%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
    "localhost",
    "api.sunandsandstays.com",
    "127.0.0.1",
    "*.smartportfolios.co",
    "smartportfolios.ckq0nibpvq6u.us-west-1.rds.amazonaws.com",
    "opulent-halibut-9r9w7qr7g5qc7v9x-30000.app.github.dev"
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    "corsheaders",
    'knox',
    'customers',
    'property',
    'destination',
    'investors',
    'agent',
    'property_listing',
    'enquiry',
    'cancellation',
    'property_manager',
    'booking',
    'event'
    
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restserver.wsgi.application'




AUTH_USER_MODEL = 'customers.Customers'

CORS_ALLOW_ALL_ORIGINS = True
SILENCED_SYSTEM_CHECKS = ["auth.E003"]
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Using MySQL engine
        'NAME': os.environ.get('MYSQL_DB', 'stayvillas'),
        'USER': os.environ.get('MYSQL_USER', 'stockrobot'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', '10gXWOqeaf'),
        'HOST': os.environ.get('MYSQL_HOST', 'api.stayvillas.co'),
        'PORT': os.environ.get('MYSQL_PORT', '5432'),  # Default MySQL port
    }
}
#  the local configurations are added to file
#local setup for if server is not working
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Use PostgreSQL engine
#         'NAME': os.environ.get('POSTGRES_DB', 'postgres'), #check database name 
#         'USER': os.environ.get('POSTGRES_USER', 'postgres'),  #default
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '123456'),  # put your password
#         'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),  # Host for local development
#         'PORT': os.environ.get('POSTGRES_PORT', '5432'),  # PostgreSQL default port
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_DIR = os.path.join (BASE_DIR, "static")


STATIC_URL ='/static/'# path to read css with local (probably)
STATICFILES_DIRS = [
        os.path.join (BASE_DIR, "static"),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import sentry_sdk

sentry_sdk.init(
    dsn="https://343f07974b6db30273660bf67a127cb8@o4508080204611584.ingest.us.sentry.io/4508080205987840",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)