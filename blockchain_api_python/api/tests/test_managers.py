from django.test import TestCase

from api.errors import InitialBlockError
from api.models import Block


class BlockManageTest(TestCase):

    def test_create_new_block_error(self):
        with self.assertRaises(InitialBlockError):
            Block.block_manager.create_new_block(data={}, previous_hash="0")

    def test_raise_error_initial_block(self):
        with self.assertRaises(InitialBlockError):
            Block.block_manager.create_initial_block()
            Block.block_manager.create_initial_block()
