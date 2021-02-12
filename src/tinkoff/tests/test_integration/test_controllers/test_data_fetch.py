import pytest

from tinkoff.controllers.statistic import TinkoffStatisticController
from tinkoff.controllers.exceptions import InvalidOperationsPiecharRequest


@pytest.fixture()
def statistic_controller_factory(tinkoff_http_client_factory):
    def _with_tinkoff_response(tinkoff_mock_response):
        http = tinkoff_http_client_factory(tinkoff_mock_response)
        controller = TinkoffStatisticController(http=http)
        controller.http = http
        return controller
    return _with_tinkoff_response


def test_invalid_operations_piechar_response(statistic_controller_factory):
    controller = statistic_controller_factory({
        'resultCode': 'INVALID_REQUEST_DATA',
        'errorMessage': 'AUTTB15LL - Bad format. Parameter start. Invalid time format. UTC milliseconds is expected.',
        'plainMessage': 'Bad format. Parameter start. Invalid time format. UTC milliseconds is expected.',
        'trackingId': 'AUTTB15LL',
    })

    with pytest.raises(InvalidOperationsPiecharRequest):
        controller.get_operations_piechar('test-session')
