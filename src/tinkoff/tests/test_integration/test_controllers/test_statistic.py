import pytest

from decimal import Decimal

from tinkoff.controllers.exceptions import TooManyHalfMoneySpendException, TooManyQuartelryMoneySpendException
from tinkoff.controllers.statistic import TinkoffStatisticController
from tinkoff.converters import TinkoffDataConverter


@pytest.fixture()
def controller():
    return TinkoffStatisticController()


@pytest.fixture()
def current_month_operations_for_quarterly_check():
    return TinkoffDataConverter([
        {
            'amountPercent': 39.61999470957303,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 1500.0,
            },
            'spendingCategory': {
                'id': '57',
                'name': 'Переводы',
                'icon': '39',
                'parentId': '8',
            },
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
    ])()


@pytest.fixture()
def current_month_operations_for_half_check():
    return TinkoffDataConverter([
        {
            'amountPercent': 39.61999470957303,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100.0,
            },
            'spendingCategory': {
                'id': '57',
                'name': 'Переводы',
                'icon': '39',
                'parentId': '8',
            },
            'groupBy': 'Переводы',
        },
        {
            'amountPercent': 11.644298151316375,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 10000.0,
            },
            'spendingCategory': {
                'id': '55',
                'name': 'Транспорт',
                'icon': '36',
                'parentId': '4',
            },
            'groupBy': 'Транспорт',
        },
    ])()


@pytest.fixture()
def required_budget():
    return {
        'Переводы': Decimal(1000),
        'Транспорт': Decimal(800),
    }


def test_alert_about_quarter_of_required_budget(
    controller, current_month_operations_for_quarterly_check, required_budget,
):
    with pytest.raises(TooManyQuartelryMoneySpendException) as exc_info:
        controller.check_budget_for_quarterly_spending(current_month_operations_for_quarterly_check, required_budget)

    assert str(exc_info.value) == (
        'Too many quarter of budget spending: \n'
        'Spends for Переводы – 1500.0. Allowed is 1000\n'
    )


def test_alert_about_half_or_required_budget(
    controller, current_month_operations_for_half_check, required_budget,
):
    with pytest.raises(TooManyHalfMoneySpendException) as exc_info:
        controller.check_budget_for_half_spending(current_month_operations_for_half_check, required_budget)

    assert str(exc_info.value) == (
        'Too many half of budget spending: \n'
        'Spends for Транспорт – 10000.0. Allowed is 800\n'
    )
