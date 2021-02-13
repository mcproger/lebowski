from base_controller import BaseController
from tinkoff.controllers.auth import TinkoffAuthController
from tinkoff.converters import TinkoffDataConverter
from tinkoff.controllers.exceptions import (
    ImproperlySignedUpException, MoreThanHalfOfTheBudgetSpentException, MoreThanQuarterOfTheBudgetSpentException,
    TooManyMoneySpendException, InvalidOperationsPiecharRequest,
)
from tinkoff.helpers import operations_piechar_url
from tinkoff.http_client import TinkoffHttpClient
from tinkoff.repositories.dumb_repository import DumbRepository


class TinkoffStatisticController(BaseController):
    def __init__(self, http=None, auth=None, data_repository=None) -> None:
        self.http = http or TinkoffHttpClient()
        self.auth = auth or TinkoffAuthController(self.http)
        self.data_repository = data_repository or DumbRepository()

    def run(self) -> str:
        try:
            session_id = self.auth.run()
        except ImproperlySignedUpException:
            return None  # NOTE add loggin about failure

        try:
            raw_current_spending = self.get_operations_piechar(session_id)
        except InvalidOperationsPiecharRequest:
            return None  # NOTE add logging here  about failure

        current_spending = TinkoffDataConverter(raw_current_spending)()
        required_budget = self.data_repository.get_required_budget()

        return self.get_info_about_current_spenndings_state(current_spending, required_budget)

    def get_operations_piechar(self, session_id: str) -> dict:
        try:
            response = self.http.make_request(
                'GET',
                url=operations_piechar_url(session=session_id),
            )
            return response['payload']['aggregated']
        except KeyError:
            raise InvalidOperationsPiecharRequest

    def get_info_about_current_spenndings_state(self, current_spending: dict, required_budget) -> str:
        half_spends_message = quarter_spends_message = ''

        try:
            self.check_budget_for_half_spending(current_spending, required_budget)
        except MoreThanHalfOfTheBudgetSpentException as exc_info:
            half_spends_message = str(exc_info)

        try:
            self.check_budget_for_quarterly_spending(current_spending, required_budget)
        except MoreThanQuarterOfTheBudgetSpentException as exc_info:
            quarter_spends_message = str(exc_info)

        if half_spends_message or quarter_spends_message:
            return f'{half_spends_message}\n{quarter_spends_message}'

        return 'At the moment your running expenses are ok'

    def check_budget_for_quarterly_spending(self, current_budget: dict, required_budget: dict) -> None:
        quarterly_spending_index = 4

        try:
            self._check_budget(current_budget, required_budget, quarterly_spending_index)
        except TooManyMoneySpendException as exc_info:
            raise MoreThanQuarterOfTheBudgetSpentException(f'More than a quarter of the budget spent: \n{exc_info}')

    def check_budget_for_half_spending(self, current_budget: dict, required_budget: dict) -> None:
        half_spending_index = 2

        try:
            self._check_budget(current_budget, required_budget, half_spending_index)
        except TooManyMoneySpendException as exc_info:
            raise MoreThanHalfOfTheBudgetSpentException(f'More than a half of the budget spent: \n{exc_info}')

    def _check_budget(
        self, current_spending: dict, required_budget: dict, spending_index: int,
    ) -> None:
        too_many_spends = []

        for spending_type, spending_value in current_spending.items():
            allowed_budget = required_budget.get(spending_type, 0)

            if spending_value >= allowed_budget / spending_index:
                too_many_spends.append(f'Spends for {spending_type} – {spending_value}. Allowed is {allowed_budget}\n')

        if too_many_spends:
            raise TooManyMoneySpendException(''.join(too_many_spends))
