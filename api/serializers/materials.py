from apps_data.course.models import Material

from rest_framework import serializers
from rest_framework_extensions.mixins import PaginateByMaxMixin



class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ('url', 'course', 'title', 'description', 'file',
                  'slug', 'pdf_download_link', 'pdf_link', 'pdf_viewer')
        read_only_fields = ('created', 'modified',)

