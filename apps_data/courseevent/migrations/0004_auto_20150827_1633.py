# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0003_auto_20150818_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('text', models.TextField(verbose_name='Text')),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='announcement',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='archivieren'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_forumlink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Forum'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_homeworklink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Aufgabe'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_lessonlink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Lektion'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_listlink',
            field=models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Liste'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_publishlink',
            field=models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='publishlink'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_shortlink',
            field=models.BooleanField(default=True, help_text='die wichtigsten Links werden als Kurzlinks angezeigt.\n        Es sollte nicht mehr als 10 Kurzlinks geben', verbose_name='Kurzlink'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='optional',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='price',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='has_published_decendants',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum: Forum wird publiziert'), ('lesson', 'Unterricht: Lektion wird publiziert '), ('announcements', 'Link zu Ank\xfcndigungsliste'), ('homework', 'Link zu einer Hausaufgabe'), ('last_posts', 'Link zu den neuesten Beitr\xe4ge'), ('private', 'Link zum Privatbereich der Kursteilnehmer'), ('header', '\xdcberschrift'), ('participants', 'Link zur Teilnehmerliste')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='start_date',
            field=models.DateField(help_text='im Format Tag.Monat.Jahr angeben', null=True, verbose_name='Startdatum', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'nicht \xf6ffentlich'), ('1', 'zur Buchung ge\xf6ffnet'), ('1', 'Buchung abgeschlossen'), ('2', 'Vorschau')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'nicht ver\xf6ffentlicht'), ('1', 'offen zur Buchung'), ('a', 'Vorschau')]),
        ),
        migrations.AlterField(
            model_name='homework',
            name='classlesson',
            field=models.OneToOneField(verbose_name='Bezug auf einen Lernabschnitt?', to='lesson.ClassLesson'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateField(null=True, verbose_name='Abgabedatum', blank=True),
        ),
        migrations.AlterField(
            model_name='studentswork',
            name='workers',
            field=models.ManyToManyField(related_name='teammembers', verbose_name='Team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='comment',
            name='studentswork',
            field=models.ForeignKey(to='courseevent.StudentsWork'),
        ),
    ]
