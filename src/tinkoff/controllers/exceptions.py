from __future__ import annotations


class ImproperlySignedUpException(Exception):
    pass


class TooManyMoneySpendException(Exception):
    pass


class MoreThanQuarterOfTheBudgetSpentException(Exception):
    pass


class MoreThanHalfOfTheBudgetSpentException(Exception):
    pass


class InvalidOperationsPiecharRequest(Exception):
    pass
