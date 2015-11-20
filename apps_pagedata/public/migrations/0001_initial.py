# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import apps_pagedata.public.models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPublicPages',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('pagecode', models.CharField(help_text='Der Seitencode ordnet die Textchunks eindeutig zu html Seiten zu. Die Views greifen die Seiten \xfcber den Seitencode ab.', max_length=20, serialize=False, verbose_name='Seitencode', primary_key=True)),
                ('text', froala_editor.fields.FroalaField(help_text='Dieser Text wird als html chunk auf der Seite integriert. Der pagecode ordnet die Seite zu', verbose_name='Textchunk', blank=True)),
                ('title', models.CharField(help_text='Der Seitentitel wird ebenfalls benutzt zum Aufbau der  zugeordenten html Seite', max_length=200, verbose_name='Seitentitel', blank=True)),
                ('description', models.CharField(help_text='wird nicht nach aussen angezeigt.', max_length=250, verbose_name='interne Beschreibung der Seite')),
                ('banner', models.ImageField(help_text='Optional kann ein Banner hochgeladen werden, dass nach aussen angezeigt werden kann.', upload_to=apps_pagedata.public.models.foto_location, verbose_name='Banner', blank=True)),
                ('meta_keywords', models.CharField(help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description')),
                ('meta_title', models.CharField(help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel')),
                ('slug', models.SlugField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\xd6ffentliche statische Seite',
                'verbose_name_plural': '\xd6ffentliche statische Seiten',
            },
        ),
    ]
