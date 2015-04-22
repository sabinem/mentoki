# -*- coding: utf-8 -*-
from django.db import models

class DocFile(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


import datetime

from django.db import models


class File(models.Model):

    upload = models.FileField(upload_to="uploads/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)