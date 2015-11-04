# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps_pagedata.textchunks.models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0006_auto_20151018_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publictextchunks',
            options={'verbose_name': '\xd6ffentliche statische Seite', 'verbose_name_plural': '\xd6ffentliche statische Seiten'},
        ),
        migrations.AddField(
            model_name='publictextchunks',
            name='meta_description',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publictextchunks',
            name='meta_keywords',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publictextchunks',
            name='meta_title',
            field=models.CharField(default='x', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='banner',
            field=models.ImageField(help_text='Optional kann ein Banner hochgeladen werden, dass nach aussen angezeigt werden kann.', upload_to=apps_pagedata.textchunks.models.foto_location, verbose_name='Banner', blank=True),
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='description',
            field=models.CharField(help_text='wird nicht nach aussen angezeigt.', max_length=250, verbose_name='interne Beschreibung der Seite'),
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='pagecode',
            field=models.CharField(help_text='Der Seitencode ordnet die Textchunks eindeutig zu html Seiten zu. Die Views greifen die Seiten \xfcber den Seitencode ab.', max_length=20, serialize=False, verbose_name='Seitencode', primary_key=True),
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='text',
            field=froala_editor.fields.FroalaField(help_text='Dieser Text wird als html chunk auf der Seite integriert. Der pagecode ordnet die Seite zu', verbose_name='Textchunk'),
        ),
        migrations.AlterField(
            model_name='publictextchunks',
            name='title',
            field=models.CharField(help_text='Der Seitentitel wird ebenfalls benutzt zum Aufbau der  zugeordenten html Seite', max_length=200, verbose_name='Seitentitel'),
        ),
    ]
