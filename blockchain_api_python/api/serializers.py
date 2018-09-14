from rest_framework import serializers

from api.models import Account, Block


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'balance']
        read_only_fields = ['id', 'balance']


class AccountValueSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField()

    class Meta:
        model = Account
        fields = ['value']


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'timestamp', 'data', 'previous_hash', 'hash']
        read_only_fields = ['id', 'timestamp', 'data', 'previous_hash', 'hash']
