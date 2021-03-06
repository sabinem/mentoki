# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import autoslug.fields
import django.db.models.deletion
import apps_data.course.models.course
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(help_text='Arbeitstitel f\xfcr Deinen Kurs. Er ist nicht \xf6ffentlich\n                    sichtbar.', max_length=100, verbose_name='Kurstitel')),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', unique=True, editable=False)),
                ('excerpt', models.TextField(help_text='Diese Kurzbeschreibung dient sp\xe4ter als Vorlage\n                    bei der Ausschreibung Deiner Kurse', verbose_name='Kurze Zusammenfassung / Abstrakt', blank=True)),
                ('target_group', models.TextField(help_text='Die Zielgruppe f\xfcr Deinen Kurs.', verbose_name='Zielgruppe', blank=True)),
                ('prerequisites', models.TextField(help_text='Welches Vorwissen wird in Deinem\n                    Kurses Voraussetzung?', verbose_name='Voraussetzungen', blank=True)),
                ('project', models.TextField(help_text='Was nehmen Teilnehmer aus Deinem Kurs f\xfcr sich mit?', verbose_name='Teilnehmerprojekt', blank=True)),
                ('structure', models.TextField(help_text='Gib eine Gliederung Deines Kurses an', verbose_name='Gliederung', blank=True)),
                ('text', models.TextField(help_text='Hier kannst Du Deinen Kurs ausf\xfchrlich beschreiben.', verbose_name='Kursbeschreibung', blank=True)),
                ('email', models.EmailField(default='mentoki@mentoki.com', help_text='Die email-Adresse des Kursleiters oder eine\n                    Mentoki-Adresse. Bitte stimme diese Adresse mit\n                    Mentoki ab.', max_length=254, verbose_name='email Addresse f\xfcr den Kurs')),
            ],
            options={
                'verbose_name': 'Kursvorlage',
                'verbose_name_plural': 'Kursvorlagen',
            },
        ),
        migrations.CreateModel(
            name='CourseOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das\n                  Halten dieses Kurses?', verbose_name='Kursleiterbeschreibung', blank=True)),
                ('foto', models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der\n                    Kursauschreibung erscheinen soll.', upload_to=apps_data.course.models.course.foto_location, verbose_name='Kursleiter-Foto', blank=True)),
                ('display', models.BooleanField(default=True, help_text='Soll dieses Profil auf der Kursausschreibungsseite\n                    angezeigt werden?.', verbose_name='Anzeigen auf der Auschreibungsseite?')),
                ('display_nr', models.IntegerField(default=1, help_text='Dieses Feld steuert die Anzeigereihenfolge bei mehreren\n                    Kursleitern.', verbose_name='Anzeigereihenfolge')),
                ('course', models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Kursleiter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['course', 'display_nr'],
                'verbose_name': 'Kursleitung',
                'verbose_name_plural': 'Kursleitungen',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='course.CourseOwner'),
        ),
    ]
