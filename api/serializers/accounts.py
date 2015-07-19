from authentication.models import Account

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


