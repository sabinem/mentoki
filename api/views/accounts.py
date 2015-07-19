from ..serializers import *
from rest_framework import viewsets

from django.contrib.auth.models import User, Group, Permission


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
