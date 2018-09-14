from django.db import models

from api.errors import InitialBlockError


class BlockManager(models.Manager):

    def create_initial_block(self):
        if self.filter(previous_hash="0").exists():
            raise InitialBlockError()
        obj = self.create(data={'message': 'Initial block'}, previous_hash="0")
        return obj

    def create_new_block(self, data, previous_hash):
        if self.count() == 0:
            raise InitialBlockError(msg="You need an initial block.")
        obj = self.create(data=data, previous_hash=previous_hash)
        obj.make_own_hash()
        return obj

    def get_last_block_hash(self):
        if self.count() == 0:
            raise InitialBlockError(msg="You need an initial block.")
        return self.last().hash
