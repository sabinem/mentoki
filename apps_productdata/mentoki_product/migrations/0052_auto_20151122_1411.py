# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0051_auto_20151120_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_description_description',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Description Detail Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_description_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Description Mentoren Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_description_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Description Angebot Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_keywords_description',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Keywords Detail Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_keywords_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Keywords Mentoren Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_keywords_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Keywords Angebot Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_title_description',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Title Detail Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_title_mentors',
            field=models.CharField(default='Mentoki', max_length=250, verbose_name='Meta Title Mentoren Seite'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='meta_title_offers',
            field=models.CharField(default='Mentoki', help_text='HTML Meta Information zur Seite.', max_length=250, verbose_name='Meta Title Angebot Seite'),
        ),
    ]
