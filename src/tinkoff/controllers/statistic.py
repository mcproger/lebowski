from base_controller import BaseController
from tinkoff.constants import OPERATIONS_PIECHART_URL
from tinkoff.controllers.auth import TinkoffAuthController
from tinkoff.converters import TinkoffDataConverter
from tinkoff.controllers.exceptions import (
    ImproperlySignedUpException, TooManyHalfMoneySpendException, TooManyQuartelryMoneySpendException,
    TooManyMoneySpendException,
)
from tinkoff.http_client import TinkoffHttpClient
from tinkoff.repositories.dumb_repository import DumbRepository


class TinkoffStatisticController(BaseController):
    def __init__(self) -> None:
        self.http = TinkoffHttpClient()
        self.auth = TinkoffAuthController(self.http)
        self.data_repository = DumbRepository()

    def run(self) -> str:
        try:
            session_id = self.auth.run()
        except ImproperlySignedUpException:
            return None  # NOTE add notification about failure

        raw_current_spending = self.get_operations_piechar(session_id)['payload']['aggregated']
        current_spending = TinkoffDataConverter(raw_current_spending)()
        required_budget = self.data_repository.get_required_budget()

        return self.get_info_about_current_spenndings_state(current_spending, required_budget)

    def get_operations_piechar(self, session_id: str) -> dict:
        return self.http.make_request(
            'GET',
            url=OPERATIONS_PIECHART_URL.format(signed_up_session_id=session_id),
        )

    def get_info_about_current_spenndings_state(self, current_spending: dict, required_budget) -> str:
        try:
            self.check_budget_for_half_spending(current_spending, required_budget)
        except TooManyHalfMoneySpendException as exc_info:
            return str(exc_info)

        try:
            self.check_budget_for_quarterly_spending(current_spending, required_budget)
        except TooManyQuartelryMoneySpendException as exc_info:
            return str(exc_info)

        return 'At the moment your running expenses are ok '

    def check_budget_for_quarterly_spending(self, current_budget: dict, required_budget: dict) -> None:
        quarterly_spending_index = 4

        try:
            self._check_budget(current_budget, required_budget, quarterly_spending_index)
        except TooManyMoneySpendException as exc_info:
            raise TooManyQuartelryMoneySpendException(f'Too many quarter of budget spending: \n{exc_info}')

    def check_budget_for_half_spending(self, current_budget: dict, required_budget: dict) -> None:
        half_spending_index = 2

        try:
            self._check_budget(current_budget, required_budget, half_spending_index)
        except TooManyMoneySpendException as exc_info:
            raise TooManyHalfMoneySpendException(f'Too many half of budget spending: \n{exc_info}')

    def _check_budget(
        self, current_spending: dict, required_budget: dict, spending_index: int,
    ) -> None:
        too_many_spends = []

        for spending_type, spending_value in current_spending.items():
            if spending_value >= required_budget[spending_type] / spending_index:
                too_many_spends.append(f'Spends for {spending_type} – {spending_value}')

        if too_many_spends:
            raise TooManyMoneySpendException('\n'.join(too_many_spends))
