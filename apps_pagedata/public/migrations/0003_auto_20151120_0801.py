# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps_pagedata.public.models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_staticpublicpages_template_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpublicpages',
            name='banner',
            field=models.ImageField(help_text='Optional', upload_to=apps_pagedata.public.models.foto_location, verbose_name='Banner', blank=True),
        ),
        migrations.AlterField(
            model_name='staticpublicpages',
            name='text',
            field=froala_editor.fields.FroalaField(verbose_name='Text', blank=True),
        ),
        migrations.AlterField(
            model_name='staticpublicpages',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Seitentitel', blank=True),
        ),
    ]
