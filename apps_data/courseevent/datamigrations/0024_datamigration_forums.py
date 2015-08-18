# -*- coding: utf-8 -*-0023_auto_20150617_1038.py

"""
shell script:
from data.courseevent.models import Forum as NewForum
from apps.forum.models import Forum as OldForum

forums = OldForum.objects.all()

for f in forums:
       forum = NewForum(title=f.title, text=f.text, oldforum=f,
          courseevent= f.courseevent, created=f.created, modified=f.modified, can_have_threads=False, display_nr=1)
       forum.insert_at(None)
       forum.save()

NewForum.objects.rebuild()
"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_forums(apps, schema_editor):
    OldForum = apps.get_model("forum", "Forum")
    NewForum = apps.get_model("courseevent", "Forum")


    for forum in OldForum.objects.all():
        forum = NewForum(title=forum.title,
                         text=forum.text,
                         courseevent= forum.courseevent,
                         oldforum = forum,
                         created=forum.created,
                         modified=forum.modified,
                         can_have_threads=False,
                         display_nr=1)

        forum.insert_at(None)
        forum.save()

    NewForum.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20150622_0703'),
    ]

    operations = [
        migrations.RunPython(transfer_forums)
    ]
