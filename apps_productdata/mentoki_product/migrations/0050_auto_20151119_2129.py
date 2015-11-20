# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0049_auto_20151119_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='courseproductgroup',
            name='meta_title',
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_description_description',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_description_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_description_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_keywords_description',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_keywords_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_keywords_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_title_description',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_title_mentors',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='meta_title_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Titel'),
        ),
    ]
