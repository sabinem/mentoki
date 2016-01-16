# coding: utf-8

"""
Entry point for local development.
"""

from __future__ import absolute_import, unicode_literals
from .base import *

# Debug settings
DEBUG = True

# additional thirdparty apps
INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
)

# ssl settings
SSLIFY_DISABLE = True

# overwrites media root
MEDIA_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'media')

# overwrite email backend
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#TODO: how can I overwrite just that one setting for DEBUG in templates?
# templates overwrites
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                'django.core.context_processors.request',
                "django.contrib.messages.context_processors.messages",
            ],
            'debug': DEBUG
        },
    },
]

# overwriting raven
RAVEN_CONFIG = {'dsn': ''}

import braintree
BRAINTREE_ENVIRONMENT = braintree.Environment.Sandbox


EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}