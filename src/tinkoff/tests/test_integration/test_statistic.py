import pytest

from tinkoff.controllers.exceptions import TooManyHalfMoneySpendException, TooManyQuartelryMoneySpendException
from tinkoff.controllers.statistic import TinkoffStatisticController
from tinkoff.converters import TinkoffDataConverter
from tinkoff.repositories.dumb_repository import DumbRepository


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
                'value': 950000.0,
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
            'amountPercent': 17.926102732035254,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 150000.0,
            },
            'spendingCategory': {
                'id': '60',
                'name': 'Фастфуд',
                'icon': '38',
                'parentId': '3',
            },
            'groupBy': 'Фастфуд',
        },
        {
            'amountPercent': 13.396070689195916,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 675000.0,
            },
            'spendingCategory': {
                'id': '24',
                'name': 'Рестораны',
                'icon': '32',
                'parentId': '3',
            },
            'groupBy': 'Рестораны',
        },
        {
            'amountPercent': 12.548114844211893,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 1000000.23,
            },
            'spendingCategory': {
                'id': '25',
                'name': 'Супермаркеты',
                'icon': '10',
                'parentId': '3',
            },
            'groupBy': 'Супермаркеты',
        },
        {
            'amountPercent': 11.644298151316375,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 1000000.0,
            },
            'spendingCategory': {
                'id': '55',
                'name': 'Транспорт',
                'icon': '36',
                'parentId': '4',
            },
            'groupBy': 'Транспорт',
        },
        {
            'amountPercent': 2.508471751235734,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 1000500.0,
            },
            'spendingCategory': {
                'id': '51',
                'name': 'Другое',
                'icon': '33',
                'parentId': '8',
            },
            'groupBy': 'Другое',
        },
        {
            'amountPercent': 1.358178075254707,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 500100.0,
            },
            'spendingCategory': {
                'id': '16',
                'name': 'Кино',
                'icon': '37',
                'parentId': '2',
            },
            'groupBy': 'Кино',
        },
        {
            'amountPercent': 0.5728370113319172,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 200500.0,
            },
            'spendingCategory': {
                'id': '31',
                'name': 'Мобильная связь',
                'icon': '42',
                'parentId': '5',
            },
            'groupBy': 'Мобильная связь',
        },
        {
            'amountPercent': 0.3714201267023076,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500.0,
            },
            'spendingCategory': {
                'id': '32',
                'name': 'Связь',
                'icon': '9',
                'parentId': '5',
            },
            'groupBy': 'Связь',
        },
        {
            'amountPercent': 0.05451190914287599,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 25000.0,
            },
            'spendingCategory': {'id': '61', 'name': 'Услуги банка'},
            'groupBy': 'Услуги банка',
        },
    ])()


@pytest.fixture()
def current_month_operations_for_half_check():
    return TinkoffDataConverter([
        {
            'amountPercent': 39.61999470957303,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 10050000.0,
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
            'amountPercent': 17.926102732035254,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '60',
                'name': 'Фастфуд',
                'icon': '38',
                'parentId': '3',
            },
            'groupBy': 'Фастфуд',
        },
        {
            'amountPercent': 13.396070689195916,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '24',
                'name': 'Рестораны',
                'icon': '32',
                'parentId': '3',
            },
            'groupBy': 'Рестораны',
        },
        {
            'amountPercent': 12.548114844211893,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '25',
                'name': 'Супермаркеты',
                'icon': '10',
                'parentId': '3',
            },
            'groupBy': 'Супермаркеты',
        },
        {
            'amountPercent': 11.644298151316375,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '55',
                'name': 'Транспорт',
                'icon': '36',
                'parentId': '4',
            },
            'groupBy': 'Транспорт',
        },
        {
            'amountPercent': 2.508471751235734,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '51',
                'name': 'Другое',
                'icon': '33',
                'parentId': '8',
            },
            'groupBy': 'Другое',
        },
        {
            'amountPercent': 1.358178075254707,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '16',
                'name': 'Кино',
                'icon': '37',
                'parentId': '2',
            },
            'groupBy': 'Кино',
        },
        {
            'amountPercent': 0.5728370113319172,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 100500,
            },
            'spendingCategory': {
                'id': '31',
                'name': 'Мобильная связь',
                'icon': '42',
                'parentId': '5',
            },
            'groupBy': 'Мобильная связь',
        },
        {
            'amountPercent': 0.3714201267023076,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 200500,
            },
            'spendingCategory': {
                'id': '32',
                'name': 'Связь',
                'icon': '9',
                'parentId': '5',
            },
            'groupBy': 'Связь',
        },
        {
            'amountPercent': 0.05451190914287599,
            'amount': {
                'currency': {'code': 643, 'name': 'RUB', 'strCode': '643'},
                'value': 10060,
            },
            'spendingCategory': {'id': '61', 'name': 'Услуги банка'},
            'groupBy': 'Услуги банка',
        },
    ])()


@pytest.fixture()
def required_budget():
    return DumbRepository().get_required_budget()


def test_alert_about_quarter_of_required_budget(
    controller, current_month_operations_for_quarterly_check, required_budget,
):
    with pytest.raises(TooManyQuartelryMoneySpendException) as exc_info:
        controller.check_budget_for_quarterly_spending(current_month_operations_for_quarterly_check, required_budget)

    assert str(exc_info.value) == (
        'Too many quarter of budget spending: \n'
        'Spends for Переводы – 950000.0\nSpends for Фастфуд – 150000.0\n'
        'Spends for Рестораны – 675000.0\nSpends for Супермаркеты – 1000000.23\n'
        'Spends for Транспорт – 1000000.0\nSpends for Другое – 1000500.0\n'
        'Spends for Кино – 500100.0\nSpends for Мобильная связь – 200500.0\n'
        'Spends for Связь – 100500.0\nSpends for Услуги банка – 25000.0'
    )


def test_alert_about_half_or_required_budget(
    controller, current_month_operations_for_half_check, required_budget,
):
    with pytest.raises(TooManyHalfMoneySpendException) as exc_info:
        controller.check_budget_for_half_spending(current_month_operations_for_half_check, required_budget)

    assert str(exc_info.value) == (
        'Too many half of budget spending: \n'
        'Spends for Переводы – 10050000.0\nSpends for Фастфуд – 100500\n'
        'Spends for Рестораны – 100500\nSpends for Супермаркеты – 100500\n'
        'Spends for Транспорт – 100500\nSpends for Другое – 100500\n'
        'Spends for Кино – 100500\nSpends for Мобильная связь – 100500\n'
        'Spends for Связь – 200500\nSpends for Услуги банка – 10060'
    )
