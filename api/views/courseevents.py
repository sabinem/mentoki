from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response

from ..serializers import *
from apps_data.courseevent.models import CourseEvent
from django.contrib.auth.models import User
from ..permissions import *


from rest_framework.decorators import detail_route

class CourseEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    permission_classes = (CourseIsOwnerOrReadOnly,)
    serializer_class = CourseCompleteSerializer
    queryset = CourseEvent.objects.all()

    def get_queryset(self, **kwargs):
        if self.request.user.is_staff:
            return Course.objects.all()
        else:
            return Course.objects.teaching(user=self.request.user)


