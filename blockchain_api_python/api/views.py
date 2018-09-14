from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.errors import NotEnoughFundsError, InitialBlockError
from api.models import Account, Block
from api.serializers import AccountValueSerializer, AccountSerializer, BlockSerializer


class SetZeroAccountUpdateViewSet(UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def update(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            obj.initialize()
            last_hash = Block.block_manager.get_last_block_hash()
            Block.block_manager.create_new_block({'message': "The value of the balance is set to zero."}, last_hash)
        except InitialBlockError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'The account is now at zero'}, status=status.HTTP_200_OK)


class TransactionAccountUpdateViewSet(UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountValueSerializer

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            value = serializer.validated_data['value']
            try:
                obj.transaction(value)
                obj.refresh_from_db()
                last_hash = Block.block_manager.get_last_block_hash()
                Block.block_manager.create_new_block(
                    {
                        "message": "Successful transaction.",
                        "value": value,
                        "balance": obj.balance
                    },
                    last_hash
                )
            except NotEnoughFundsError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except InitialBlockError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'balance': obj.balance}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockTransactionsListView(ListModelMixin, GenericViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
