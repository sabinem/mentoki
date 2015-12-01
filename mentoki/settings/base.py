# coding: utf-8

"""
Settings for mentoki project
"""

# path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
)
#path above the project
BASE_DIR_PROJECT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Debug settings
DEBUG = False

# hosts
ALLOWED_HOSTS = ['*']

#admins
ADMINS = (('Sabine', 'sabine.maennel@gmail.com'),)

#site
SITE_ID = 1

# installed apps django
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
)

# installed apps thirdparty
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
)

# installed apps mentoki
INSTALLED_APPS += (
    'accounts',

    'apps_accountdata.userprofiles',

    'apps_customerdata.customer',

    'apps_productdata.mentoki_product',

    'apps_pagedata.textchunks',
    'apps_pagedata.public',

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
    'apps_public.storefront',
    'apps_public.checkout',

    'apps_core.core',
    'apps_core.email',
    'apps_core.webhooks',
)

# custom user model
AUTH_USER_MODEL = 'accounts.User'

# middleware
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
)

# urls
ROOT_URLCONF = 'mentoki.urls'

# wsgi
WSGI_APPLICATION = 'mentoki.wsgi.application'

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

MAINTENANCE_MODE = False


# Internationalization

# language settings
gettext = lambda x: x

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en',_('English')),
    ('de',_('German')),
    ('es',_('Spanish')),
)

LANGUAGE_CODE = 'de'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale','apps_internal','classroom'),
)

# date time formats

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'd.m.Y'


# TODO: brauche ich dieses setup so? Oder ist es veraltet?
# static and media urls
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

# ignore certain urls
import re
IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

# email settings for google mail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# mentoki mail adresses
MENTOKI_INFO_EMAIL = u'mentoki@mentoki.com'
MENTOKI_COURSE_EMAIL = u'mentoki@mentoki.com'

# database caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

# sentry
RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN')
}

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
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
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
        'data.userdata': {
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

    },
}

# 3rd party apps:

# Login and redirect urls
from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy("account_login")
LOGIN_REDIRECT_URL = reverse_lazy("desk:redirect")
LOGOUT_URL = reverse_lazy("home:home")
COURSE_LIST_URL = reverse_lazy('storefront:list')

# 3rd party app allauth:
# allauth backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
# other allauth settings
from django.core.urlresolvers import reverse_lazy
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

#  3rd party app markdown:
MARKDOWN_EDITOR_SKIN = 'simple'

# 3rd party app Froala Editor

# Froala settings
# different activation key for each website: staging, production, etc.)
FROALA_EDITOR_OPTIONS = {
    'key': os.environ.get('FROALA_ACTIVATION_KEY'),
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

# 3rd party app fontawesome: location of css file
FONTAWESOME_CSS_URL = '/static/font-awesome-4.4.0/css/font-awesome.min.css'

# 3rd party app Braintree:

# braintree configuration for testing in the sandbox
BRAINTREE = {
    'merchant_id':os.environ.get('BRAINTREE_MERCHANT_ID'),
    'merchant_account_id_chf':os.environ.get('BRAINTREE_MERCHANT_ACCOUNT_ID_CHF'),
    'merchant_account_id_eur':os.environ.get('BRAINTREE_MERCHANT_ACCOUNT_ID_EUR'),
    'public_key':os.environ.get('BRAINTREE_PUBLIC_KEY'),
    'private_key':os.environ.get('BRAINTREE_PRIVATE_KEY'),
}



