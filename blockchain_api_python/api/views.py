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
            # the object instance is obtained
            obj = self.get_object()
            # the account is reset to zero
            obj.initialize()
            # a new block is created
            last_hash = Block.block_manager.get_last_block_hash()
            Block.block_manager.create_new_block({'message': "The value of the balance is set to zero."}, last_hash)
        except InitialBlockError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'The account is now at zero'}, status=status.HTTP_200_OK)


class TransactionAccountUpdateViewSet(UpdateModelMixin, GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountValueSerializer

    def update(self, request, *args, **kwargs):
        # the object instance is obtained
        obj = self.get_object()
        serializer = self.serializer_class(data=request.data)
        # the data is validated with the serializer
        if serializer.is_valid():
            value = serializer.validated_data['value']
            try:
                # the value is added to the account
                obj.transaction(value)
                # the value of the object is updated after the transaction
                obj.refresh_from_db()
                # get the hash of the last block
                last_hash = Block.block_manager.get_last_block_hash()
                # a new block is created with the values of the transaction
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
