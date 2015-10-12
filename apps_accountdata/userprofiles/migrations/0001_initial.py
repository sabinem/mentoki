# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings
import model_utils.fields
import apps_accountdata.userprofiles.models.mentor


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorsProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das\n                  Halten dieses Kurses?', verbose_name='Kursleiterbeschreibung', blank=True)),
                ('foto', models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der\n                    Kursauschreibung erscheinen soll.',
                                           upload_to=apps_accountdata.userprofiles.models.mentor.foto_location, verbose_name='Kursleiter-Foto', blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Kursleiter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentoren',
            },
        ),
    ]
