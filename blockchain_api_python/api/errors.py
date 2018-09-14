class NotEnoughFundsError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "There are not enough funds for this transaction."
        super(NotEnoughFundsError, self).__init__(msg)


class InitialBlockError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "There is already an initial block."
        super(InitialBlockError, self).__init__(msg)
