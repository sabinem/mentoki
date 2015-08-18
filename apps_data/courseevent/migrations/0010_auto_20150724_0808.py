# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0057_auto_20150724_0808'),
        ('courseevent', '0009_auto_20150722_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Thema')),
                ('text', models.TextField(verbose_name='Text der Ank\xfcndigung: Vorsicht Bilder werden noch nicht mitgeschickt')),
                ('due_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('item_type', models.CharField(max_length=15, choices=[('forum', 'forum'), ('lesson', 'lesson or lesson block'), ('anouncements', 'announcements'), ('homework', 'homework')])),
                ('item_nr', models.IntegerField()),
                ('published', models.BooleanField(default=False)),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published')),
                ('is_start_item', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentsWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Thema')),
                ('text', models.TextField(verbose_name='Text der Ank\xfcndigung: Vorsicht Bilder werden noch nicht mitgeschickt')),
                ('published', models.BooleanField(default=False)),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='status',
        ),
        migrations.AddField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='you_okay',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(help_text='Diese Zusammenfassung erscheint auf der Kursliste.', verbose_name='Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='max_participants',
            field=models.IntegerField(help_text='E', null=True, verbose_name='Teilnehmeranzahl', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='nr_weeks',
            field=models.IntegerField(help_text='Die Anzahl der Wochen, die der Kurs dauern soll, nur bei gef\xfchrten Kursen.', null=True, verbose_name='Wochenanzahl', blank=True),
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
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
        migrations.AddField(
            model_name='menu',
            name='forum',
            field=models.ForeignKey(blank=True, to='courseevent.Forum', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='homework',
            field=models.ForeignKey(blank=True, to='courseevent.Homework', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='lesson',
            field=models.ForeignKey(blank=True, to='course.Lesson', null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='courseevent',
            field=models.ForeignKey(to='courseevent.CourseEvent'),
        ),
    ]
