"""
Django settings for pet_project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import datetime
from pathlib import Path
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

LOCAL_APPS = [
    'innotter.apps.InnotterConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_celery_beat',
    'django_celery_results',

]

INSTALLED_APPS = CORE_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'innotter.middleware.JWTMiddleware',
]

ROOT_URLCONF = 'pet_project.urls'

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

WSGI_APPLICATION = 'pet_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DATABASE_ENGINE'),
#         'HOST': os.getenv('DATABASE_HOST'),
#         'USER': os.getenv('DATABASE_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'PORT': os.getenv('DATABASE_PORT'),
#         'NAME': os.getenv('POSTGRES_DB'),
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'HOST': os.getenv('DATABASE_HOST'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'PORT': os.getenv('DATABASE_PORT'),
        'NAME': os.getenv('POSTGRES_DB'),
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    'DEFAULT_FILTER_BACKENDS':
        [
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
        ],


    'DEFAULT_AUTHENTICATION_CLASSES': [
        'innotter.authentication.JWTAuthentication',
    ]
}

AUTH_USER_MODEL = 'innotter.User'

JWT_AUTH = {
    'JWT_SECRET_KEY': os.getenv('SECRET_KEY'),
    'JWT_ALGORITHM': os.getenv('JWT_ALGORITHM'),
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=float(os.getenv('WT_EXPIRATION_DELTA'))),
    'JWT_AUTH_HEADER_PREFIX': os.getenv('JWT_AUTH_HEADER_PREFIX'),
}

DEBUG = True



CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Warsaw'
CELERY_IMPORTS = ('innotter.tasks',)


CELERY_BEAT_SCHEDULE = {
    "scheduled_task": {
        "task": "innotter.tasks.celery_unblock_page",
        "schedule": 5.0,
    }
}




EMAIL_BACKEND = 'django_ses.SESBackend'


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_SES_REGION_NAME = 'eu-north-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-north-1.amazonaws.com'

AWS_STORAGE_BUCKET_NAME = 'django-images-forartsake'
# AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_REGION_NAME = 'eu-north-1'

DEFAULT_FILE_STORAGE = 'pet_project.storage.MediaStore'

