from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Account
from api.serializers import TransactionSerializer, AccountSerializer


class InitializeAccountUpdateView(UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.initialize()
        return Response({'message': 'The account is now at zero'}, status=status.HTTP_200_OK)


class TransactionAccountUpdateView(UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = TransactionSerializer

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            valor = serializer.validated_data['valor']
            obj.transaction(valor)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryTransactionsListView(ListModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
