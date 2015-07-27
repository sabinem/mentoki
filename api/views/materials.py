from ..serializers import *
from rest_framework import viewsets
from ..permissions import *
from rest_framework.decorators import list_route
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps_data.course.models.material import Material

class MaterialViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (CoursePartIsOwnerOrReadOnly,)

