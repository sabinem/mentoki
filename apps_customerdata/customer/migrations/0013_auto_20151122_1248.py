# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20151122_1247'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prebooking',
            unique_together=set([('email', 'interested_in_learning')]),
        ),
    ]
