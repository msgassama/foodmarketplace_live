"""
Django settings for foodMarketplace project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'accounts.apps.AccountsConfig',
    'vendor.apps.VendorConfig',
    'menu.apps.MenuConfig',
    'marketplace.apps.MarketplaceConfig',
    'customers.apps.CustomersConfig',
    'orders.apps.OrdersConfig',
    'django.contrib.gis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'orders.request_object.RequestObjectMiddleware', # custom middleware created to access the request object in orders models.py
    'vendor.request_object.RequestObjectMiddleware', # custom middleware created to access the request object in vendor models.py
]

ROOT_URLCONF = 'foodMarketplace.urls'

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
                'accounts.context_processors.get_vendor',
                'accounts.context_processors.get_google_api',
                'marketplace.context_processors.get_cart_counter',
                'marketplace.context_processors.get_cart_amounts',
                'accounts.context_processors.get_user_profile',
                'accounts.context_processors.get_paypal_client_id',
                'accounts.context_processors.get_stripe_api_key',
            ],
        },
    },
]

WSGI_APPLICATION = 'foodMarketplace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': os.getenv('ENGINE'),
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

AUTH_USER_MODEL = 'accounts.User'

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# MEDIA FILES CONFIGURATION
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# MESSAGES TAGS
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    50: 'critical',
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

# EMAIL CONFIGURATION
EMAIL_HOST=os.getenv('EMAIL_HOST')
EMAIL_PORT=int(os.getenv('EMAIL_PORT'))
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=bool(os.getenv('EMAIL_USE_TLS'))
DEFAULT_FROM_EMAIL=os.getenv('DEFAULT_FROM_EMAIL')


# GOOGLE API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# USE_THOUSAND_SEPARATOR = True



os.environ['PATH'] = os.path.join(BASE_DIR, '.venv\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, '.venv\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, '.venv\Lib\site-packages\osgeo\gdal303.dll')

# PAYPAL
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')

# STRIPE
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')

SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"