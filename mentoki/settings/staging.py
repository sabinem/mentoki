
# coding: utf-8
"""
Entry point for the staging site.
"""

from __future__ import absolute_import, unicode_literals
from .base import *


# ssl settings
SSLIFY_DISABLE = True

# static and media root
STATIC_ROOT = os.path.join(BASE_DIR, 'htdocs', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'htdocs', 'media')