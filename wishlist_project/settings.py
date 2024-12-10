"""
Django settings for wishlist_project project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from django.conf.global_settings import STATIC_ROOT, MEDIA_ROOT
from google.oauth2 import service_account

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xf+qf_pk2nf02mh(!g%9_do4l))igl@d0er249=&_rl0^ysww9'

# SECURITY WARNING: don't run with debug turned on in production!
# if os.getenv('GAE_INSTANCE'):
#     DEBUG = False
# else:
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'travel_wishlist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wishlist_project.urls'

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

WSGI_APPLICATION = 'wishlist_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#Default settings - will work at App Engine GCP
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'places',
        'USER': 'traveler',
        'PASSWORD': os.getenv('TRAVELER_PW'),
        'HOST': '/cloudsql/wishlist-443603:us-central1:wishlist-db-mysql',
        'PORT': '3306'
    }
}

#connect to the same database when this code is running on our computer
#here, need to connect via the cloud proxy
#test if we are running locally?  modify database settings for local development
if not os.getenv('GAE_INSTANCE'):
    #app is not running at GAE, use local settings
    DATABASES['default']['HOST'] = '127.0.0.1'
    # DATABASES= {
    #     'default':{
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    #     }
    # }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
#Specify location to copy static files to when running python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

#Where in the file system to save user-uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'wishlist/../media') this was original code

if not os.getenv('GAE_INSTANCE'): #Local development settings - not running at GCP
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

else: #GCP settings - running on GCP
    # Static files - where are they stored?
    GS_STATIC_FILE_BUCKET = 'wishlist-443603.appspot.com'
    STATIC_URL = f'https://storage.cloud.google.com/{GS_STATIC_FILE_BUCKET}/static/'

    # Media files - uploaded by user
    GS_BUCKET_NAME = 'wishlist-user-upload-images-zil'
    MEDIA_URL = f'https://storage.cloud.google.com/{GS_BUCKET_NAME}/media/'
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file('travel_credentials.json')

    # Tell Django what libraries to use to access static files and media files
    STORAGES = {
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
        'default': {
            'BACKEND': 'storages.backends.gcloud.GoogleCloudStorage',
        }
    }

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'