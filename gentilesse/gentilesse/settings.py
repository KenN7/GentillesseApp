"""
Django settings for gentilesse project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6(l5qykw3wuyxx53qwrin0qkr&oo^%f)3e$9m)11vpjn$5+h$0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'colorful',
    'tracker',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gentilesse.urls'

WSGI_APPLICATION = 'gentilesse.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.messages.context_processors.messages',
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC+1'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

RISPY_TEMPLATE_PACK = 'bootstrap3'

BOOTSTRAP3 = {
        # The URL to the jQuery JavaScript file
        #'jquery_url': '//code.jquery.com/jquery.min.js',
        'jquery_url': STATIC_URL + 'js/jquery.min.js',
        # The Bootstrap base URL
        #'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.2.0/',
        'base_url': STATIC_URL,
        # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
        'css_url': None,
        # The complete URL to the Bootstrap CSS file (None means no theme)
        'theme_url': None,
        # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
        'javascript_url': None,
    }
