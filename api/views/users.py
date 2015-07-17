from ..serializers import *
from rest_framework import viewsets

from django.contrib.auth.models import User, Group, Permission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
