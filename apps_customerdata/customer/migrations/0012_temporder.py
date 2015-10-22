# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0030_courseproductgroup_display_nr'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0011_auto_20151021_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('by_authenticated_user', models.BooleanField(default=False)),
                ('for_self', models.BooleanField(default=True)),
                ('participant_email', models.EmailField(default='g@gmail.com', max_length=254, verbose_name='Email des Teilnehmers', blank=True)),
                ('participant_first_name', models.CharField(max_length=40, blank=True)),
                ('participant_last_name', models.CharField(max_length=40, blank=True)),
                ('participant_username', models.CharField(max_length=40, blank=True)),
                ('courseproduct', models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True)),
                ('user', models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Teilnehmer als Benutzer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
