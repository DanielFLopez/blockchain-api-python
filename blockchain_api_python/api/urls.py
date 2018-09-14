from rest_framework import routers

from api.views import SetZeroAccountUpdateViewSet, TransactionAccountUpdateViewSet, BlockTransactionsListView

router = routers.DefaultRouter()

router.register(r'initialize', SetZeroAccountUpdateViewSet, base_name='initialize')
router.register(r'transaction', TransactionAccountUpdateViewSet, base_name='transaction')
router.register(r'history', BlockTransactionsListView)

urlpatterns = router.urls
