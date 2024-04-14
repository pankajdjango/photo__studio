"""
Django settings for PK_Photo_Studio project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os,sys

is_production = 1 if '/var/run/apache2' in f"{os.environ.get('APACHE_RUN_DIR')}" else 0

if bool(is_production):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    ALLOWED_HOSTS = ["5.181.217.57","photostudio.pankajtrsrewa.com"]
else :
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.append('/home/pankaj/study/cicd/config')
    ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Set DEBUG mode based on the environment
DEBUG = not is_production

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
from config import DATABASE_CONFIG, SECRET_KEY
# SECURITY WARNING: don't run with debug turned on in production!

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ps_webapp',
    'restapi',
    'account',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.Custom404Middleware',
    'account.middleware.URLHistoryMiddleware',
]

ROOT_URLCONF = 'PK_Photo_Studio.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PK_Photo_Studio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import psycopg2.extensions
if not is_production:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DATABASE_CONFIG['NAME'],
            'USER': DATABASE_CONFIG['USER'],
            'PASSWORD': DATABASE_CONFIG['PASSWORD'],
            'HOST': DATABASE_CONFIG['HOST'],
            'PORT': DATABASE_CONFIG['PORT'],
            'OPTIONS': {
                    'client_encoding' : 'UTF8',
                    #'timezone:' : 'Asia/Kolkata',
                    # 'isolation_level':psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DATABASE_CONFIG['NAME'],
            'USER': DATABASE_CONFIG['USER'],
            'PASSWORD': DATABASE_CONFIG['PASSWORD'],
            'HOST': DATABASE_CONFIG['HOST'],
            'PORT': DATABASE_CONFIG['PORT'],
            'OPTIONS': {
                    'client_encoding' : 'UTF8',
                    #'timezone:' : 'Asia/Kolkata',
                    #'isolation_level':psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#custome settings
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / 'static'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR,]
TIME_ZONE = 'Asia/Kolkata'
