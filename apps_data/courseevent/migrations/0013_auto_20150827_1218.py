# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0012_announcement_archive'),
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
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('studentswork', models.ForeignKey(to='courseevent.StudentsWork')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum: Forum wird publiziert'), ('lesson', 'Unterricht: Lektion wird publiziert '), ('announcements', 'Link zu Ank\xfcndigungsliste'), ('homework', 'Link zu einer Hausaufgabe'), ('last_posts', 'Link zu den neuesten Beitr\xe4ge'), ('private', 'Link zum Privatbereich der Kursteilnehmer'), ('header', '\xdcberschrift'), ('participants', 'Link zur Teilnehmerliste')]),
        ),
    ]
