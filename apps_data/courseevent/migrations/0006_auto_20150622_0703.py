# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150621_2213'),
        ('courseevent', '0005_auto_20150621_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='oldforum',
            field=models.ForeignKey(blank=True, to='forum.Forum', null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='oldsubforum',
            field=models.ForeignKey(related_name='Unterforum_alt', blank=True, to='forum.SubForum', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='oldpost',
            field=models.ForeignKey(blank=True, to='forum.Post', null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='oldthread',
            field=models.ForeignKey(blank=True, to='forum.Thread', null=True),
        ),
    ]
