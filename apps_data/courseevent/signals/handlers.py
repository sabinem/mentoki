from django.dispatch import receiver
from .signals import example_signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import Signal
from django.conf import settings
from .models.menu import ClassroomMenuItem
from .models.forum import Forum


@receiver(example_signal)
def example_signal_handler(sender, **kwargs):
    print kwargs['arg1']
    print kwargs['arg2']


@receiver(post_save, sender=ClassroomMenuItem)
def publish_forum_handler(sender, instance, created, **kwargs):
    print "+++++++++"
    print "hello i am here"
    if ClassroomMenuItem.instance.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.forum_item:
        forum = Forum(forum=ClassroomMenuItem.instance.forum)
        forum.publish = True
        forum.save()

