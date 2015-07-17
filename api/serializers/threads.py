from django.forms import widgets
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from apps_data.courseevent.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User
from rest_framework_extensions.mixins import DetailSerializerMixin

class ThreadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Thread
        fields = ('url', 'title', 'courseevent', 'forum', 'text', 'author', 'created', 'modified')
