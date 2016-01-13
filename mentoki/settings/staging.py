# coding: utf-8

"""
Entry point for the production site.
"""

from __future__ import absolute_import, unicode_literals
from .base import *

# sentry
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

# static and media root
STATIC_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'media')


# ssl settings
#SSLIFY_DISABLE = True
# set braintree environment: so far it is the sandbox
import braintree
BRAINTREE_ENVIRONMENT = braintree.Environment.Sandbox

# django-email-bandit
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')