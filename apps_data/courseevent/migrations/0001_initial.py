# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import mailqueue.models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Betreff')),
                ('text', models.TextField(verbose_name='Text')),
                ('published', models.BooleanField(default=False, help_text='Beim Ver\xf6ffentlichen wird die Ank\xfcndigung an alle Kursteilnehmer\n        und Mentoren verschickt:\n        ', verbose_name='ver\xf6ffentlichen?')),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), verbose_name='ver\xf6ffentlicht am', monitor='published')),
                ('is_archived', models.BooleanField(default=False, help_text='Archivierte Ver\xf6ffentlichungen sind im Klassenzimmer nicht mehr zu sehen.\n        ', verbose_name='archivieren')),
                ('mail_distributor', models.TextField(null=True, verbose_name=mailqueue.models.MailerMessage, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassroomMenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('item_type', models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum: Forum wird publiziert'), ('lesson', 'Unterricht: Lektion wird publiziert '), ('announcements', 'Link zu Ank\xfcndigungsliste'), ('homework', 'Link zu einer Hausaufgabe'), ('last_posts', 'Link zu den neuesten Beitr\xe4ge'), ('private', 'Link zum Privatbereich der Kursteilnehmer'), ('header', '\xdcberschrift'), ('participants', 'Link zur Teilnehmerliste')])),
                ('is_shortlink', models.BooleanField(default=False, help_text='die wichtigsten Links werden als Kurzlinks angezeigt.\n        Es sollte nicht mehr als 10 Kurzlinks geben', verbose_name='Kurzlink')),
                ('is_publishlink', models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='publishlink')),
                ('is_listlink', models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Liste')),
                ('is_forumlink', models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Forum')),
                ('is_lessonlink', models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Lektion')),
                ('is_homeworklink', models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Aufgabe')),
                ('active', models.BooleanField(default=True)),
                ('optional', models.BooleanField(default=True)),
                ('display_nr', models.IntegerField(help_text='An welcher Position im Men\xfc soll der Men\xfcpunkt angezeigt werden?', verbose_name='Reihenfolge Nummer')),
                ('display_title', models.CharField(max_length=200)),
                ('is_start_item', models.BooleanField(help_text='Welcher Men\xfcpunkt soll im Klassenzimmer als\n            erstes angesprungen werden?', verbose_name='Ist Startpunkt')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(help_text='Kurstitel unter dem dieser Kurs ausgeschrieben wird.', max_length=100, verbose_name='Kurstitel')),
                ('start_date', models.DateField(help_text='im Format Tag.Monat.Jahr angeben', null=True, verbose_name='Startdatum', blank=True)),
                ('nr_weeks', models.IntegerField(help_text='Die Anzahl der Wochen, die der Kurs dauern soll, nur bei gef\xfchrten Kursen.', null=True, verbose_name='Wochenanzahl', blank=True)),
                ('max_participants', models.IntegerField(null=True, verbose_name='Teilnehmeranzahl', blank=True)),
                ('event_type', models.CharField(default='selflearn', max_length=12, verbose_name='Kursart', choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'Selbstlernen mit Unterst\xfctzung')])),
                ('status_external', models.CharField(default='0', max_length=2, verbose_name='externer Status', choices=[('0', 'nicht \xf6ffentlich'), ('1', 'zur Buchung ge\xf6ffnet'), ('1', 'Buchung abgeschlossen'), ('2', 'Vorschau')])),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking']), monitor='status_external')),
                ('booking_closed_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking_closed']), monitor='status_external')),
                ('active', models.BooleanField(default=True)),
                ('status_internal', models.CharField(default='0', max_length=2, verbose_name='interner Status', choices=[('0', 'nicht ver\xf6ffentlicht'), ('1', 'offen'), ('a', 'Vorschau')])),
                ('accepted_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['accepted']), monitor='status_external')),
                ('review_ready_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['review']), monitor='status_external')),
                ('excerpt', models.TextField(help_text='Diese Zusammenfassung erscheint auf der Kursliste.', verbose_name='Abstrakt', blank=True)),
                ('video_url', models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True)),
                ('text', models.TextField(verbose_name='freie Kursbeschreibung', blank=True)),
                ('format', models.TextField(verbose_name='Kursformat', blank=True)),
                ('workload', models.TextField(verbose_name='Arbeitsbelastung', blank=True)),
                ('project', models.TextField(verbose_name='Teilnehmernutzen', blank=True)),
                ('structure', models.TextField(verbose_name='Gliederung', blank=True)),
                ('target_group', models.TextField(help_text='Zielgruppe, wie sie in der Kursausschreibung erscheinen soll.', verbose_name='Zielgruppe', blank=True)),
                ('prerequisites', models.TextField(verbose_name='Voraussetzungen', blank=True)),
                ('price', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('you_okay', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseEventParticipation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('hidden', models.BooleanField(default=False, verbose_name='versteckt')),
                ('hidden_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Forums-Titel')),
                ('text', models.TextField(help_text='Dieser Text wird den Forumsbeitr\xe4gen vorangestellt und leitet die Kursteilnehmern an, ihre\n                  Beitr\xe4ge zu schreiben.', verbose_name='Ausf\xfchrliche Beschreibung des Forums', blank=True)),
                ('description', models.CharField(help_text='Die Kurzbeschreibung erscheint auf der \xdcbersichtsseite der Foren.', max_length=200, verbose_name='Kurzbeschreibung', blank=True)),
                ('display_nr', models.IntegerField(help_text='nicht nach aussen sichtbar', verbose_name='Anzeigereihenfolge')),
                ('can_have_threads', models.BooleanField(default=True, help_text='Steuert, ob Beitr\xe4ge in diesem Unterforum gemacht werden k\xf6nnen,\n                  oder ob es nur zur Gliederung dient.', verbose_name='Beitr\xe4ge erlaubt')),
                ('hidden', models.BooleanField(default=False, verbose_name='versteckt')),
                ('hidden_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden')),
                ('published', models.BooleanField(default=False, help_text='Zeigt an, ob das Forum im Klassenzimmer sichtbar ist.', verbose_name='ver\xf6ffentlicht', editable=False)),
                ('publish_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published')),
                ('has_published_decendants', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Foren',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('hidden', models.BooleanField(default=False, verbose_name='versteckt')),
                ('hidden_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='StudentsWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('text', models.TextField(verbose_name='Text')),
                ('comments', models.TextField(verbose_name='Kommentare', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen')),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published')),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('hidden', models.BooleanField(default=False, verbose_name='versteckt')),
                ('hidden_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=100, verbose_name='Titel f\xfcr Deinen Beitrag')),
                ('post_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(related_name='thread_author', to=settings.AUTH_USER_MODEL)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('forum', models.ForeignKey(to='courseevent.Forum', on_delete=django.db.models.deletion.PROTECT)),
                ('last_author', models.ForeignKey(related_name='last_post_author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Beitrag',
                'verbose_name_plural': 'Beitr\xe4ge',
            },
        ),
    ]
