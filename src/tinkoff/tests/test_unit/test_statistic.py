from __future__ import annotations

from decimal import Decimal

import pytest

from tinkoff.controllers.exceptions import (
    MoreThanHalfOfTheBudgetSpentException,
    MoreThanQuarterOfTheBudgetSpentException,
)
from tinkoff.helpers import convert_raw_tinkoff_data


@pytest.fixture()
def current_month_operations_for_quarterly_check():
    return convert_raw_tinkoff_data(
        [  # NOTE use pydantic for this
            {
                'amountPercent': 39.61999470957303,
                'amount': {
                    'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                    'value': 300.0,
                },
                'spendingCategory': {'id': '57', 'name': 'Переводы', 'icon': '39', 'parentId': '8'},
                'groupBy': 'Переводы',
            },
            {
                'amountPercent': 11.644298151316375,
                'amount': {
                    'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                    'value': 100.0,
                },
                'spendingCategory': {
                    'id': '55',
                    'name': 'Транспорт',
                    'icon': '36',
                    'parentId': '4',
                },
                'groupBy': 'Транспорт',
            },
        ]
    )


@pytest.fixture()
def current_month_operations_for_half_check():
    return convert_raw_tinkoff_data(
        [
            {
                'amountPercent': 39.61999470957303,
                'amount': {
                    'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                    'value': 100.0,
                },
                'spendingCategory': {'id': '57', 'name': 'Переводы', 'icon': '39', 'parentId': '8'},
                'groupBy': 'Переводы',
            },
            {
                'amountPercent': 11.644298151316375,
                'amount': {
                    'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                    'value': 1100.0,
                },
                'spendingCategory': {
                    'id': '55',
                    'name': 'Транспорт',
                    'icon': '36',
                    'parentId': '4',
                },
                'groupBy': 'Транспорт',
            },
        ]
    )


@pytest.fixture()
def required_budget():
    return {'Переводы': Decimal(1000), 'Транспорт': Decimal(2000)}


def test_alert_about_quarter_of_required_budget(
    statistic_controller, current_month_operations_for_quarterly_check, required_budget
):
    with pytest.raises(MoreThanQuarterOfTheBudgetSpentException) as exc_info:
        statistic_controller.check_budget_for_quarterly_spending(
            current_month_operations_for_quarterly_check, required_budget
        )

    assert str(exc_info.value) == (
        'More than a quarter of the budget spent: \n'
        'Spends for Переводы – 300.0. Allowed is 1000\n'
    )


def test_alert_about_half_or_required_budget(
    statistic_controller, current_month_operations_for_half_check, required_budget
):
    with pytest.raises(MoreThanHalfOfTheBudgetSpentException) as exc_info:
        statistic_controller.check_budget_for_half_spending(
            current_month_operations_for_half_check, required_budget
        )

    assert str(exc_info.value) == (
        'More than a half of the budget spent: \n'
        'Spends for Транспорт – 1100.0. Allowed is 2000\n'
    )
