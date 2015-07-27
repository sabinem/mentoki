from django.forms import widgets
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from apps_data.courseevent.models.forum import Forum
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User
from rest_framework_extensions.mixins import DetailSerializerMixin

class ForumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Forum
        fields = ('url', 'title', 'courseevent', 'text', 'display_nr', 'can_have_threads')

