from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import Signal
from django.conf import settings
from ..models.menu import ClassroomMenuItem
from ..models.forum import Forum
#from .handlers import publish_forum_handler

example_signal = Signal(providing_args=['arg1', 'arg2'])


#post_save.connect(publish_forum_handler, sender=ClassroomMenuItem,
#                  dispatch_uid="publish_forum_handler")

import django.dispatch

pizza_done = Signal(providing_args=["toppings", "size"])