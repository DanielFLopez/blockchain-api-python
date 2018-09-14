from django.test import TestCase

from api.models import Account, Block


class AccountTest(TestCase):
    fixtures = ['initial_data']

    def test_string_representation(self):
        account = Account.objects.get(pk=1)
        self.assertEqual(str(account), str(account.balance))


class BlockTest(TestCase):
    fixtures = ['initial_data']

    def test_string_representation(self):
        block = Block.block_manager.create_initial_block()
        self.assertEqual(str(block), block.hash)
