"""
Django settings for contabilidad project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '71rdg0g(kikgw^dduu%dt2nm(p=g^p-y**w!8&@bx66(dlkkq3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True) or True

ALLOWED_HOSTS_STRING = os.environ.get('ALLOWED_HOSTS', '*') or '*'

ALLOWED_HOSTS = ALLOWED_HOSTS_STRING.split(',')

ENABLE_DEBUG_TOOLBAR = os.environ.get('ENABLE_DEBUG_TOOLBAR', False) or False


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'rest_framework_swagger',
    'oauth2_provider',
    'rest_framework_tracking',
    'billing',
    'avatar',
    'ocr',
    'anymail',
    'customer',
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

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)  # CRUM middleware

ROOT_URLCONF = 'contabilidad.urls'

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

WSGI_APPLICATION = 'contabilidad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'postgres') or 'postgres',
        'USER': os.environ.get('DATABASE_USER', 'postgres') or 'postgres',
        'HOST': os.environ.get('DATABASE_HOST', 'db') or 'db',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', '') or '',
        'PORT': os.environ.get('DATABASE_PORT', 5432) or 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend', ),
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'es-mx') or 'es-mx'

TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Monterrey') or 'America/Monterrey'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

if os.environ.get('AWS_BUCKET', False) or False:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', '')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'utils.storage.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'utils.storage.MediaStorage'

OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False

SITE_ID = 1

# Mail setting
HAS_EMAIL_SETTING_MAILGUN = os.environ.get('EMAIL_SETTING_MAILGUN', False)

if HAS_EMAIL_SETTING_MAILGUN:

    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', '')
    if MAILGUN_API_KEY:
        ANYMAIL = {
            'MAILGUN_API_KEY': MAILGUN_API_KEY,
            'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_DOMAIN'),
        }

        EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', 'localhost')
        EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
        EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
        EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', 25)
        EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}