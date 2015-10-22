# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0008_auto_20151019_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='participant_email',
            field=models.EmailField(default='g@gmail.com', max_length=254, verbose_name='Email des Teilnehmers'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, verbose_name='Teilnehmer als Benutzer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Kundenemail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(verbose_name='Kunde, der bezahlt hat', blank=True, to='customer.Customer', null=True),
        ),
    ]
