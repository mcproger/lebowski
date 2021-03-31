from __future__ import annotations

import typing
from decimal import Decimal

from tinkoff.repositories.base import BaseRepository

REQURIED_BUDGET = {  # example
    'Переводы': Decimal(300),
    'Фастфуд': Decimal(100),
    'Супермаркеты': Decimal(200),
    'Рестораны': Decimal(700),
    'Транспорт': Decimal(400),
    'Другое': Decimal(400),
    'Кино': Decimal(200),
    'Мобильная связь': Decimal(80),
    'Связь': Decimal(40),
    'Услуги банка': Decimal(10),
    'Аптеки': Decimal(500),
}


class DumbRepository(BaseRepository):
    def get_required_budget(self) -> typing.Dict[str, Decimal]:
        return REQURIED_BUDGET
