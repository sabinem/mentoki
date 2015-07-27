from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response

from ..serializers import *
from apps_data.course.models.course import Course
from django.contrib.auth.models import User
from ..permissions import *
from rest_framework_extensions.mixins import NestedViewSetMixin


from rest_framework.decorators import detail_route

class CourseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    permission_classes = (CourseIsOwnerOrReadOnly,)
    serializer_class = CourseCompleteSerializer
    queryset = Course.objects.all()

    def get_queryset(self, **kwargs):
        if self.request.user.is_staff:
            return Course.objects.all()
        else:
            return Course.objects.teaching(user=self.request.user)


class CoursesPerTeacherList(generics.ListCreateAPIView):
    """
    special query for courses per teacher
    """
    permission_classes = (CourseIsOwnerOrReadOnly,)
    serializer_class = CourseCompleteSerializer
    queryset = Course.objects.all()
