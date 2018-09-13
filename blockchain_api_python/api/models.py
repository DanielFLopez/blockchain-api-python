from django.core.validators import MinValueValidator
from django.db import models, transaction


class Account(models.Model):

    balance = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    @classmethod
    def transaction(cls, amount):
        with transaction.atomic():
            account = (cls.objects.select_for_update().get(id=1))

            if (account.balance + amount) < 0:
                print("There are not enough funds for this transaction.")
            else:
                account.balance += amount
                account.save()

        return account

    def __str__(self):
        return self.balance
