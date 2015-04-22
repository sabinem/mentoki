# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_coursematerial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursematerial',
            old_name='menu_item',
            new_name='is_menu_item',
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='document_link',
            field=models.CharField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
