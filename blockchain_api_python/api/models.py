import hashlib as hasher

from django.contrib.postgres.fields import JSONField
from django.core.validators import MinValueValidator
from django.db import models, transaction

from api.errors import NotEnoughFundsError
from api.managers import BlockManager


class Account(models.Model):

    balance = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    @classmethod
    def initialize(cls):
        with transaction.atomic():
            account = (cls.objects.select_for_update().get(id=1))
            account.balance = 0
            account.save()

    @classmethod
    def transaction(cls, amount):
        with transaction.atomic():
            account = (cls.objects.select_for_update().get(id=1))
            if (account.balance + amount) < 0:
                raise NotEnoughFundsError()
            else:
                account.balance += amount
                account.save()
        return account

    def __str__(self):
        return str(self.balance)


class Block(models.Model):

    timestamp = models.DateTimeField(auto_now=True)
    data = JSONField()
    previous_hash = models.CharField(max_length=500)
    hash = models.CharField(max_length=500)

    objects = models.Manager()
    block_manager = BlockManager()

    def make_own_hash(self):
        sha = hasher.sha256()
        sha.update((str(self.pk) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode())
        self.hash = sha.hexdigest()
        self.save()

    def __str__(self):
        return self.hash
