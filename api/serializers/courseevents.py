from django.forms import widgets
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from apps_data.courseevent.models.courseevent import CourseEvent
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from django.contrib.auth.models import User
from rest_framework_extensions.mixins import DetailSerializerMixin

class CourseEventSerializer(serializers.HyperlinkedModelSerializer):
    teachersrecord = serializers.ReadOnlyField()

    class Meta:
        model = CourseEvent
        fields = ('url', 'title', 'slug', 'excerpt', 'teachersrecord', 'target_group', 'prerequisites', 'project', 'structure', 'text', 'email')


