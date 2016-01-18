# coding=utf-8
# ------------------------------------------------------------------------
# Settings for mentoki project
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# General Path Settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
)

BASE_DIR_PROJECT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# ------------------------------------------------------------------------
# Standard Django Settings

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (('Sabine', 'sabine.maennel@gmail.com'),)

SITE_ID = 1

# ------------------------------------------------------------------------
# Installed django apps (standard configuration
# plus django-suit for the admin

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects'
)

# ------------------------------------------------------------------------
# Installed third party apps

INSTALLED_APPS += (
    'braces',
    'model_utils',
    'mptt',
    'autoslug',
    'activelink',
    'floppyforms',
    'froala_editor',
    'maintenancemode',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'extra_views',
    'fontawesome',
    'mailqueue',
    'pagedown',
    'django_markdown',
    'formtools',
    'seohelper',
    'bandit',
)

# ------------------------------------------------------------------------
# Custom Apps

INSTALLED_APPS += (
    'accounts',

    'apps_accountdata.userprofiles',

    'apps_customerdata.customer',

    'apps_productdata.mentoki_product',

    'apps_pagedata.public',

    'apps_data.course',
    'apps_data.courseevent',
    'apps_data.material',
    'apps_data.lesson',
    'apps_data.notification',

    'apps_internal.desk',
    'apps_internal.coursebackend',
    'apps_internal.classroom',

    'apps_public.newsletter',
    'apps_public.contact',
    'apps_public.home',
    'apps_public.storefront',
    'apps_public.checkout',

    'apps_core.core',
    'apps_core.email',
    'apps_core.webhooks',
)

# ------------------------------------------------------------------------
# Custom User Model

AUTH_USER_MODEL = 'accounts.User'

# ------------------------------------------------------------------------
# Middleware
# - includes SSLify
# - django-maintenance-mode
# - django-redirects
# what else?

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
)

# ------------------------------------------------------------------------
# url file

ROOT_URLCONF = 'mentoki.urls'

# ------------------------------------------------------------------------
# wsgi Application

WSGI_APPLICATION = 'mentoki.wsgi.application'

# ------------------------------------------------------------------------
# database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
	    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
	    'HOST': os.environ.get('DATABASE_HOST'),
    }
}

# ------------------------------------------------------------------------
# internationalization
# - only language so far: German


# language settings
gettext = lambda x: x

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('de',_('German')),
)

LANGUAGE_CODE = 'de'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale','apps_internal','classroom'),
)

# ------------------------------------------------------------------------
# Date Time settings

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd.m.Y'

# ------------------------------------------------------------------------
# Media and static files
#
# TODO: das neue media und static file statement hatte einen Fehler!
# deshalb steht es in Kommentare, bei Gelegenheit ersetzten!

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# templates
#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': ['templates'],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.contrib.auth.context_processors.auth',
#                'django.template.context_processors.debug',
#                'django.template.context_processors.i18n',
#                'django.template.context_processors.media',
#                'django.template.context_processors.static',
#                'django.template.context_processors.tz',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
)

# ------------------------------------------------------------------------
# Fehlermeldungen unterdrücken für bestimmte urls

import re
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

# ------------------------------------------------------------------------
# google mail ist das Email backend

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# ------------------------------------------------------------------------
# mentoki emails: werden sie beide gebraucht?

MENTOKI_INFO_EMAIL = u'mentoki@mentoki.com'
MENTOKI_COURSE_EMAIL = u'mentoki@mentoki.com'

# ------------------------------------------------------------------------
# database caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table_public',
        'TIMEOUT': None
    }
}

# ------------------------------------------------------------------------
# Logging muss noch überarbeitet werden

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s][%(module)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'paymentfile': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'payments.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        'publicfile': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'public.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        'datafile': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'data.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        # log for usersignup and account handling events
        'file_usersignup': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'usersignup.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        # log for handling of userprofile data
        'file_data_userprofile': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'userprofile_data.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        # log for handling of userprofile data
        'file_classroom': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'classroom_display.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        # log for handling of userprofile data
        'file_courseevent': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'courseevent_data.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        # log for handling of email
        'file_email': {
            'filename': os.path.join(BASE_DIR, 'logfiles', 'email_sendlog.log' ),
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,  # 500 kB
            'backupCount': 4  ,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        # logs user signup activity such as user creation
        # and also userdata updates
        # app 'accounts'
        'activity.usersignup': {
            'level': 'DEBUG',
            'handlers': ['file_usersignup'],
            'propagate': False,
        },
        # logs handling of user profile data
        # app 'accountdata'
        'data.userprofile': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['sentry'],
            'propagate': False,
        },
        'sentry': {
            'level': 'INFO',
            'handlers': ['sentry'],
            'propagate': False,
        },
        'activity.users': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'activity.payments': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'data.productdata': {
            'level': 'DEBUG',
            'handlers': ['datafile'],
            'propagate': False,
        },
        'public.offerpages': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'activity.lessoncopy': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'activity.lessonview': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'activity.courseeventupdate': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'display.classroom' : {
            'level': 'DEBUG',
            'handlers': ['file_classroom'],
            'propagate': False,
        },
        'data.courseevent' : {
            'level': 'DEBUG',
            'handlers': ['file_courseevent'],
            'propagate': False,
        },
        'email.sendout' : {
            'level': 'DEBUG',
            'handlers': ['file_email'],
            'propagate': False,
        },

    },
}

# ------------------------------------------------------------------------
# Third party apps


# ------------------------------------------------------------------------
# django-maintenance-mode

MAINTENANCE_MODE = False

# ------------------------------------------------------------------------
# Konfiguration von raven für Sentry

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN')
}

# ------------------------------------------------------------------------
# Allauth and redirect urls

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy("account_login")
LOGIN_REDIRECT_URL = reverse_lazy("desk:redirect")
LOGOUT_URL = reverse_lazy("home:home")
COURSE_LIST_URL = reverse_lazy('storefront:list')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
# authenticate by email
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# email must be unique
ACCOUNT_UNIQUE_EMAIL = True
# accounts have a username
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
# the name of the email field is email
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
# an email is required
ACCOUNT_EMAIL_REQUIRED = 'True'
# email must be confirmed
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# login automatically after email has been confirmed
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SignupForm'

# ------------------------------------------------------------------------
# markdown für den newsletter der noch nicht eingebunden ist

MARKDOWN_EDITOR_SKIN = 'simple'



# ------------------------------------------------------------------------
# Froala Editor

FROALA_EDITOR_OPTIONS = {
    'key': os.environ.get('FROALA_ACTIVATION_KEY'),
}

# ------------------------------------------------------------------------
# Fontawesome wird auch für Froala gebraucht

FONTAWESOME_CSS_URL = '/static/font-awesome-4.4.0/css/font-awesome.min.css'

# ------------------------------------------------------------------------
# braintree für die Zahlungsanbindung

BRAINTREE = {
    'merchant_id':os.environ.get('BRAINTREE_MERCHANT_ID'),
    'merchant_account_id_chf':os.environ.get('BRAINTREE_MERCHANT_ACCOUNT_ID_CHF'),
    'merchant_account_id_eur':os.environ.get('BRAINTREE_MERCHANT_ACCOUNT_ID_EUR'),
    'public_key':os.environ.get('BRAINTREE_PUBLIC_KEY'),
    'private_key':os.environ.get('BRAINTREE_PRIVATE_KEY'),
}



