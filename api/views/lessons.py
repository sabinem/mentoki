from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps_data.course.models import Course, CourseOwner
from ..serializers import *
from rest_framework import viewsets
from rest_framework import generics
from braces.views import LoginRequiredMixin
from rest_framework import permissions
from rest_framework import renderers

from django.contrib.auth.models import User


class CourseMixin(object):
    queryset = Lesson.objects.all()

    def pre_save(self,obj):
        obj.course_id = self.kwargs.course_id


class LessonsAllList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self, **kwargs):
        course_pk = self.kwargs['course_pk']
        return Lesson.objects.lessons_for_course(course_id=course_pk)

class LessonBlockList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self, **kwargs):
        course_pk = self.kwargs['course_pk']
        return Lesson.block.filter(course_id=course_pk)

class LessonList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self, **kwargs):
        course_pk = self.kwargs['course_pk']
        return Lesson.block.filter(course_id=course_pk)

class LessonStepList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self, **kwargs):
        course_pk = self.kwargs['course_pk']
        return Lesson.block.filter(course_id=course_pk)


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


