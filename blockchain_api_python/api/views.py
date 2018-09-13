from rest_framework import generics


class InitializeAccountUpdateView(generics.UpdateAPIView):
    pass


class TransactionAccountUpdateView(generics.UpdateAPIView):
    pass


class HistoryTransactionsListView(generics.ListAPIView):
    pass
