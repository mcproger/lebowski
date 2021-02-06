from decimal import Decimal

from tinkoff.repositories.base import BaseRepository

REQURIED_BUDGET = {  # example
    'Переводы': Decimal(3000000),
    'Фастфуд': Decimal(1000),
    'Супермаркеты': Decimal(2000),
    'Рестораны': Decimal(7000),
    'Транспорт': Decimal(400),
    'Другое': Decimal(400),
    'Кино': Decimal(200),
    'Мобильная связь': Decimal(80),
    'Связь': Decimal(40),
    'Услуги банка': Decimal(10),
    'Аптеки': Decimal(500),
}


class DumbRepository(BaseRepository):
    def get_required_budget(self):
        return REQURIED_BUDGET
