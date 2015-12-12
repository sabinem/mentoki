
# coding: utf-8

"""
Entry point for unit tests.
"""

from __future__ import absolute_import, unicode_literals
from .base import *

# overwriting database for test
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mentoki_test'
    },
}

TESTING = True

# overwriting raven
RAVEN_CONFIG = {'dsn': ''}