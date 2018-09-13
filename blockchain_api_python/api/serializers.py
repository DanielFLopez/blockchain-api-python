from rest_framework import serializers

from api.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id']
        read_only_fields = ['id']


class TransactionSerializer(AccountSerializer):

    value = serializers.IntegerField()

    class Meta:
        model = Account
        fields = ['id', 'value']
        read_only_fields = AccountSerializer.Meta.fields + ['value']
