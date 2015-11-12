# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='currency',
            new_name='oldcurrency',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='currency',
            new_name='oldcurrency',
        ),
        migrations.AddField(
            model_name='order',
            name='newcurrency',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transaction',
            name='newcurrency',
            field=models.IntegerField(default=1),
        ),
    ]
