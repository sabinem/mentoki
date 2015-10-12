# coding: utf-8

"""
Entry point for local development.
"""

from __future__ import absolute_import, unicode_literals
from .base import *

# Debug settings
DEBUG = True
TEMPLATE_DEBUG = True

# additional thirdparty apps
INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar'
)

# ssl settings
SSLIFY_DISABLE = True

# overwrites static and media root
MEDIA_ROOT = os.path.join(BASE_DIR_PROJECT, 'ht_docs', 'media')
STATIC_ROOT = os.path.join(BASE_DIR_PROJECT, 'ht_docs', 'static')

# overwrite email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# update logging
LOGGING['loggers'].update({
    'apps_customerdata': {
         'level': 'DEBUG',
         'handlers': ['console'],
         'propagate': False,
    },
    'django.request': {
        'level': 'DEBUG',
        'handlers': ['console'],  # Dump exceptions to the console.
        'propagate': False,
    },
    '${PROJECT_NAME}': {
        'level': 'DEBUG',
        'handlers': ['console'],  # Dump app logs to the console.
        'propagate': False,
    },
})

# overwrite raven settings
RAVEN_CONFIG = {'dsn': ''}