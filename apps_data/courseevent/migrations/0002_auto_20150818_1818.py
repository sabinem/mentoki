# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20150818_1818'),
        ('courseevent', '0001_initial'),
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
                ('published', models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen?')),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), verbose_name='ver\xf6ffentlicht am', monitor='published')),
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
                ('item_type', models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('announcements', 'Ank\xfcndigungen'), ('homework', 'Hausaufgabe'), ('last_posts', 'Neueste Beitr\xe4ge'), ('private', 'Privatbereich'), ('header', '\xdcberschrift'), ('participants', 'Teilnehmerliste')])),
                ('active', models.BooleanField(default=True)),
                ('display_nr', models.IntegerField(help_text='An welcher Position im Men\xfc soll der Men\xfcpunkt angezeigt werden?', verbose_name='Reihenfolge Nummer')),
                ('display_title', models.CharField(max_length=200)),
                ('is_start_item', models.BooleanField(help_text='Welcher Men\xfcpunkt soll im Klassenzimmer als\n            erstes angesprungen werden?', verbose_name='Ist Startpunkt')),
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
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='\xdcberschrift')),
                ('text', models.TextField(verbose_name='Text')),
                ('published', models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen', editable=False)),
                ('publish_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published')),
                ('hidden', models.BooleanField(default=False, verbose_name='versteckt')),
                ('hidden_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden')),
                ('due_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
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
                ('author', models.ForeignKey(related_name='post_author', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Beitrag',
                'verbose_name_plural': 'Beitr\xe4ge',
            },
        ),
        migrations.AlterModelOptions(
            name='courseeventpubicinformation',
            options={'verbose_name': 'XCourseeventInfo'},
        ),
        migrations.AlterModelOptions(
            name='courseeventunitpublish',
            options={'verbose_name': 'XUnitPublish'},
        ),
        migrations.AddField(
            model_name='courseevent',
            name='accepted_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['accepted']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='booking_closed_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking_closed']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='format',
            field=models.TextField(verbose_name='Kursformat', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='participation',
            field=models.ManyToManyField(related_name='participation', through='courseevent.CourseEventParticipation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='prerequisites',
            field=models.TextField(verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='project',
            field=models.TextField(verbose_name='Teilnehmernutzen', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='review_ready_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['review']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='structure',
            field=models.TextField(verbose_name='Gliederung', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='target_group',
            field=models.TextField(help_text='Zielgruppe, wie sie in der Kursausschreibung erscheinen soll.', verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='text',
            field=models.TextField(verbose_name='freie Kursbeschreibung', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='video_url',
            field=models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(verbose_name='Arbeitsbelastung', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='you_okay',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='hidden_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='hidden'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='selflearn', max_length=12, choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'with coaching')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(help_text='Diese Zusammenfassung erscheint auf der Kursliste.', verbose_name='Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='max_participants',
            field=models.IntegerField(null=True, verbose_name='Teilnehmeranzahl', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='nr_weeks',
            field=models.IntegerField(help_text='Die Anzahl der Wochen, die der Kurs dauern soll, nur bei gef\xfchrten Kursen.', null=True, verbose_name='Wochenanzahl', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Startdatum', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'not public'), ('1', 'open for booking'), ('1', 'booking closed'), ('2', 'open for preview')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'not public'), ('1', 'open for booking'), ('a', 'open for preview')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='title',
            field=models.CharField(help_text='Kurstitel unter dem dieser Kurs ausgeschrieben wird.', max_length=100, verbose_name='Kurstitel'),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='prerequisites',
            field=models.TextField(verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='project',
            field=models.TextField(verbose_name='Teilnehmernutzen', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='target_group',
            field=models.TextField(verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='text',
            field=models.TextField(verbose_name='freie Kursbeschreibung', blank=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(to='courseevent.Forum', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='thread',
            name='last_author',
            field=models.ForeignKey(related_name='last_post_author', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='oldthread',
            field=models.ForeignKey(blank=True, to='forum.Thread', null=True),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='homework',
            field=models.ForeignKey(to='courseevent.Homework'),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='workers',
            field=models.ManyToManyField(related_name='teammembers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='post',
            name='oldpost',
            field=models.ForeignKey(blank=True, to='forum.Post', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='courseevent.Thread', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
