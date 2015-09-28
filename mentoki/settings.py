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

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'braces',
    #'braintree',
    'model_utils',
    'mptt',
    'autoslug',
    'activelink',
    'floppyforms',
    'froala_editor',
    #'django_prices',

    'extra_views',
    'fontawesome',

    'mailqueue',

    'pagedown',
    'django_markdown',

    'accounts',
    'customers',

    'apps_core.core',
    'apps_core.email',

    'apps_data.course',
    'apps_data.courseevent',
    'apps_data.material',
    'apps_data.lesson',

    'apps_internal.desk',
    'apps_internal.coursebackend',
    'apps_internal.classroom',

    'apps_public.newsletter',
    'apps_public.contact',
    'apps_public.home',
    'apps_public.courseoffer',
)


if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
    )

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mentoki.urls'

WSGI_APPLICATION = 'mentoki.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
	    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
	    'HOST': os.environ.get('DATABASE_HOST'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
gettext = lambda x: x

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en',_('English')),
    ('de',_('German')),
    ('es',_('Spanish')),
)


LANGUAGE_CODE = 'de_DE'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale','apps_internal','classroom'),
)

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd.m.Y'


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

CRISPY_TEMPLATE_PACK = 'semantic-ui'

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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MENTOKI_INFO_EMAIL = u'mentoki@mentoki.com'
MENTOKI_COURSE_EMAIL = u'mentoki@mentoki.com'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # formatters okay!
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
        'emailfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'email.log' ),
            'formatter': 'verbose'
        },
        'backendfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'coursebackend.log' ),
            'formatter': 'verbose'
        },
        'datafile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'data.log' ),
            'formatter': 'verbose'
        },
        'classroomfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'classroom.log' ),
            'formatter': 'verbose'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },

    },
    'loggers': {
        'apps_core.email': {
            'handlers': ['emailfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'apps_data': {
            'handlers': ['datafile'],
            'propagate': True,
            'level': 'INFO',
        },
        'apps_internal.classroom': {
            'handlers': ['classroomfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'apps_internal.coursebackend': {
            'handlers': ['backendfile'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

# Markdown
MARKDOWN_EDITOR_SKIN = 'simple'

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy("login")
LOGIN_REDIRECT_URL = reverse_lazy("desk:start")
LOGOUT_URL = reverse_lazy("home:home")

ACTIVATION_KEY = 'Eif1hsgbcC10obc=='


# Froala Editor options: custom buttons set in order to include
# 'insertHorizontalRule'
FROALA_EDITOR_OPTIONS = {
    'key': 'tckD-17B1ewrwA-7sekA2ys==',
    'inlineMode': False,
    'toolbarFixed': False,
    'minHeight': 300,
    'buttons': ['bold', 'italic', 'underline',
                        'strikeThrough', 'subscript',
                        'superscript', 'fontFamily', 'fontSize',
                        'color', 'formatBlock', 'blockStyle',
                        'inlineStyle', 'align', 'insertOrderedList',
                        'insertUnorderedList', 'outdent', 'indent',
                        'selectAll', 'createLink', 'insertImage',
                        'insertVideo', 'table', 'undo',
                        'redo', 'html',
                        'insertHorizontalRule'],
}

# Braintree set up for payments
BRAINTREE = {
    'merchant_id':os.environ.get('BRAINTREE_MERCHANT_ID'),
    'public_key':os.environ.get('BRAINTREE_PUBLIC_KEY'),
    'private_key':os.environ.get('BRAINTREE_PRIVATE_KEY'),
}

# include fontawesome (for
FONTAWESOME_CSS_URL = '/static/font-awesome-4.4.0/css/font-awesome.min.css'
