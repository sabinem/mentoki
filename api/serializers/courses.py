from django.forms import widgets
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from apps_data.course.models.course import Course
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from authentication.models import Account
from rest_framework_extensions.mixins import DetailSerializerMixin

class CourseCompleteSerializer(serializers.HyperlinkedModelSerializer):
    teachersrecord = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ('url', 'title', 'slug', 'excerpt', 'teachersrecord', 'owners', 'target_group', 'prerequisites', 'project', 'structure', 'text', 'email')


class CourseOperationalSerializer(serializers.HyperlinkedModelSerializer):
    teachersrecord = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ('url', 'title', 'slug', 'excerpt', 'teachersrecord')


#class AccountSerializer(serializers.HyperlinkedModelSerializer):
#    owner = serializers.HyperlinkedRelatedField(many=True, view_name='course-detail', read_only=True)

#    class Meta:
#        model = Account
#        fields = ('url', 'username', )