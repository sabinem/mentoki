# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0023_auto_20160119_2041'),
        ('userprofiles', '0017_auto_20151219_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('classroom_all', models.BooleanField(default=False)),
                ('announcements', models.BooleanField(default=True)),
                ('forum_all', models.BooleanField(default=False)),
                ('forum_involved', models.BooleanField(default=False)),
                ('studentswork_all', models.BooleanField(default=False)),
                ('studentswork_involved', models.BooleanField(default=True)),
                ('courseevent', models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Benachrichtigungsprofil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Benachrichtigungsprofil',
                'verbose_name_plural': 'Benachrichtigungsprofile',
            },
        ),
    ]
