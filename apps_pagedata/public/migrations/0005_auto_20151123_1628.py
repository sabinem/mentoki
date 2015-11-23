# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_pageseo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageseo',
            name='priority',
            field=models.DecimalField(default=0.5, max_digits=2, decimal_places=1),
        ),
        migrations.AddField(
            model_name='staticpublicpages',
            name='seo',
            field=models.ForeignKey(blank=True, to='public.PageSEO', null=True),
        ),
        migrations.AlterField(
            model_name='pageseo',
            name='include_in_sitemap',
            field=models.BooleanField(default=False),
        ),
    ]
