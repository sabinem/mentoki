# -*- coding: utf-8 -*-0023_auto_20150617_1038.py

"""
shell script:
AUTH_USER in settings must be still off, until the data has been transfered.

Permissisons and Groups have been empty so far.

from django.contrib.auth.models import User
from authentication.models import Account

oldusers = User.objects.all()

for o in oldusers:
    n = Account(email=o.email, username=o.username,
        first_name=o.first_name, last_name=o.last_name, last_login=o.last_login,
        is_active=o.is_active, is_staff=o.is_staff, is_superuser=o.is_superuser,
        id=o.id, password=o.password, created_at=o.date_joined)
    n.save()
"""