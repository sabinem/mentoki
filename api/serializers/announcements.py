from django.forms import widgets
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from apps_data.courseevent.models.announcement import Announcement
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User
from rest_framework_extensions.mixins import DetailSerializerMixin

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Announcement
        fields = ('url', 'title', 'courseevent', 'text', 'status', 'published_at')
