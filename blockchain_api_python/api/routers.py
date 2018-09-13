from rest_framework import routers

from api.views import InitializeAccountUpdateView, TransactionAccountUpdateView, HistoryTransactionsListView

router = routers.SimpleRouter()

router.register(r'initialize', InitializeAccountUpdateView)
router.register(r'transaction', TransactionAccountUpdateView)
router.register(r'history', HistoryTransactionsListView)

urlpatterns = router.urls
