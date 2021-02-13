import pytest

from tinkoff.controllers.statistic import TinkoffStatisticController


@pytest.fixture()
def tinkoff_http_client_factory(mocker):
    def _with_response(response):
        http_client = mocker.MagicMock()
        http_client.make_request.return_value = response
        return http_client
    return _with_response


@pytest.fixture()
def statistic_controller_factory(tinkoff_http_client_factory):
    def _with_tinkoff_response(tinkoff_mock_response=None):
        http = tinkoff_http_client_factory(tinkoff_mock_response)
        controller = TinkoffStatisticController(http=http)
        controller.http = http
        return controller
    return _with_tinkoff_response


@pytest.fixture()
def statistic_controller(statistic_controller_factory):
    return statistic_controller_factory()
