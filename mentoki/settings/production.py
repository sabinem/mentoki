# coding: utf-8

"""
Entry point for the production site.
"""

from __future__ import absolute_import, unicode_literals
from .base import *


# static and media root
STATIC_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR_PROJECT, 'htdocs', 'media')
