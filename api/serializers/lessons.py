from apps_data.course.models import *

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    parent = RecursiveField(allow_null=True,read_only=True)
    is_block = serializers.ReadOnlyField()

    class Meta:
        model = Lesson
        fields = ('is_block', 'url', 'course', 'parent', 'nr', 'title', 'text', 'description', 'material')
