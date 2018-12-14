"""
Django settings for wfpy project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # django-allauth: Required for work
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django: For numbers, text and anoher things.
    'django.contrib.humanize',
    # django-allauth : Main apps.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # easy_thumbnails: Images handle and thumbnails generator.
    'easy_thumbnails',
    # django-bootstrap4: Handling forms and inputs everywhere.
    'bootstrap4',
    # WFPY: Core (Index, Pages, etc)
    'core',
    # WFPY: Market app.
    'market',
    # WFPY: Alerts app.
    'alerts',
    # WFPY: Codex app.
    'codex',
    # pinax.messages: s an app for providing private user-to-user threaded messaging.
    # https://github.com/pinax/pinax-messages
    'pinax.messages',
    'import_export',
    'ckeditor',
]

# django-allauth: Required
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'wfpy.urls'
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
                # Core: Search Input in header, loads all items in database.
                'core.context_processors.external_data',
                # Core: User counter
                # django-grappelli: Setup
                #'core.context_processors.user_count',
                'django.template.context_processors.request',
            ],
        },
    },
]
WSGI_APPLICATION = 'wfpy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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

# django-allauth: Authentication Backends
# http://django-allauth.readthedocs.io/en/latest/installation.html#django
AUTHENTICATION_BACKENDS = (
    # django-allauth: Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # django-allauth: `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# easy-thumbnails: Extension when a image its transparent.
THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'

# easy-thumbnails: Every size for all images.
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (160, 160), 'crop': 'smart', 'upscale' : True},
        'avatar_32x32': {'size': (32, 32), 'crop': 'smart', 'upscale' : True},
        'avatar_44x44': {'size': (44, 44), 'crop': 'smart', 'upscale' : True},
        'avatar_50x50': {'size': (50, 50), 'crop': 'smart', 'upscale' : True},
        'avatar_thumb': {'size': (50, 50), 'crop': 'smart', 'upscale' : True},
        'post': {'size': (540, 0), 'crop': 'smart', 'upscale' : True},        
        'avatar_aside': {'size': (40, 40), 'crop': 'smart', 'upscale' : True},
        'avatar_header': {'size': (30, 30), 'crop': 'smart', 'upscale' : True},
        'item': {'size': (200, 200), 'crop': 'smart', 'upscale' : True},
        'item_child': {'size': (50, 50), 'crop': 'smart', 'upscale' : True},
        'order': {'size': (74, 74), 'crop': 'smart', 'upscale' : True},
        'item': {'size': (510, 287), 'crop': 'smart', 'upscale' : True},
        'quest': {'size': (510, 287), 'crop': 'smart', 'upscale' : True},
        'warframe': {'size': (510, 910), 'crop': 'smart', 'upscale' : True},
    },
}

# easy_thumbnails: Renaming the image uploads.
THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'

# django-allauth: Log In/Log Out redirection
# http://django-allauth.readthedocs.io/en/latest/configuration.html
LOGIN_REDIRECT_URL = 'feed'

# django-allauth: Email Registration Delivery
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'warframe.social@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'warframe.social@gmail.com'

# django-allauth: Sign Up Validation
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_USERNAME_MIN_LENGTH = 4

REGISTRATION_OPEN = False

# django-ckeditor: Do not check CSS class.
# https://django-ckeditor.readthedocs.io/en/latest/#if-you-want-to-use-allowedcontent

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
    }
}

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())