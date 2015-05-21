"""
Settings for netteachers project
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR_PROJECT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# get Environment Variables specific to server production/test/local
SECRET_KEY = os.environ.get('SECRET_KEY')

LOCAL_ENVIRONMENT = os.environ.get('LOCAL_ENVIROMENT')
DEBUG = bool(os.environ.get('DEBUG', False))

if DEBUG:
    TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = (('Sabine', 'sabine.maennel@gmail.com'),)

SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    # django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'raven.contrib.django.raven_compat',
    # 3rd party apps
    'floppyforms',
    'crispy_forms',
    'braces',
    'model_utils',
    'autoslug',
    'activelink',
    'django_markdown',
    # homepage
    'apps.home',
    # courses
    'apps.course',
    'apps.newsletter',
    'apps.courseevent',
    'apps.desk',
    'apps.forum',
    'apps.classroom',
    # other
    'apps.upload', 
    #'apps.email',
    # delete pdf app soon
    'apps.pdf',
    'apps.contact',
    'apps.core',
    'userauth',
)

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mentoki.urls'

WSGI_APPLICATION = 'mentoki.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        #'NAME': 'netteachers_dev',
        #'USER': 'sabinemaennel',
	    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
	    'HOST': os.environ.get('DATABASE_HOST'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
gettext = lambda x: x

LANGUAGES = (
    ('de', gettext('German')),
)

LANGUAGE_CODE = 'de_DE'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd.m.Y'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if LOCAL_ENVIRONMENT:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'media')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
)

import re
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)    

# Email
#if LOCAL_ENVIRONMENT:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#EMAIL_HOST = os.environ.get('EMAIL_HOST')
#EMAIL_PORT = os.environ.get('EMAIL_PORT')
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
#EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX')
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#SERVER_EMAIL = EMAIL_HOST_USER



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

# Logging
if LOCAL_ENVIRONMENT:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'netteachers.log',
                'formatter': 'verbose'
            },
            'console':{
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'simple'
            },
            'handler_for_my_apps': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'apps.forum': {
                'handlers': ['handler_for_my_apps'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'apps.core': {
                'handlers': ['handler_for_my_apps'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'apps.course': {
                'handlers': ['handler_for_my_apps'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'apps.classroom': {
                'handlers': ['handler_for_my_apps'],
                'propagate': True,
                'level': 'DEBUG',
            },
            'apps.desk': {
                'handlers': ['handler_for_my_apps'],
                'propagate': True,
                'level': 'DEBUG',
            },
        }
    }

    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

# Markdown
MARKDOWN_EDITOR_SKIN = 'simple'

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy("login")
LOGIN_REDIRECT_URL = reverse_lazy("desk:start")
LOGOUT_URL = reverse_lazy("home:home")