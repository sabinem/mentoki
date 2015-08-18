# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(default='info@netteachers.de', max_length=254),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='get_file_slug', editable=False, blank=True),
        ),
    ]
