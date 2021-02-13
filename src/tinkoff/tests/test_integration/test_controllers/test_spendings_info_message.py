from decimal import Decimal

import pytest

from tinkoff.converters import TinkoffDataConverter


@pytest.fixture()
def required_budget():
    return {
        'Переводы': Decimal(5000),
        'Транспорт': Decimal(6000),
    }


@pytest.fixture()
def current_spendings():
    return TinkoffDataConverter([
        {
            'amountPercent': 39.61999470957303,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 2600.0,
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
                'value': 1600.0,
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
def current_spendings_for_only_one_index():
    return TinkoffDataConverter([
        {
            'amountPercent': 39.61999470957303,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 123.0,
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
                'value': 1600.0,
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


def test_spendins_info_message(current_spendings, required_budget, statistic_controller):
    result = statistic_controller.get_info_about_current_spenndings_state(current_spendings, required_budget)

    assert result == (
        'More than a half of the budget spent: \n'
        'Spends for Переводы – 2600.0. Allowed is 5000\n'
        '\n'
        'More than a quarter of the budget spent: \n'
        'Spends for Переводы – 2600.0. Allowed is 5000\n'
        'Spends for Транспорт – 1600.0. Allowed is 6000\n'
    )


def test_spending_info_message_only_for_on_spending_index(
    current_spendings_for_only_one_index, required_budget, statistic_controller,
):
    result = statistic_controller.get_info_about_current_spenndings_state(
        current_spendings_for_only_one_index, required_budget,
    )

    assert result == '\nMore than a quarter of the budget spent: \nSpends for Транспорт – 1600.0. Allowed is 6000\n'


def test_speindg_info_message_when_spending_is_fine(required_budget, statistic_controller):
    assert statistic_controller.get_info_about_current_spenndings_state({}, required_budget) == (
        'At the moment your running expenses are ok'
    )
