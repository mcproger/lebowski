import pytest

from tinkoff.controllers.auth import TinkoffAuthController
from tinkoff.controllers.exceptions import ImproperlySignedUpException


@pytest.fixture()
def tinkoff_http_client_factory(mocker):
    def _with_response(response):
        http_client = mocker.MagicMock()
        http_client.make_request.return_value = response
        return http_client
    return _with_response


@pytest.fixture()
def controller_factory(tinkoff_http_client_factory):
    def _with_tinkoff_response(tinkoff_mock_response):
        http = tinkoff_http_client_factory(tinkoff_mock_response)
        controller = TinkoffAuthController(http)
        controller.http = http
        return controller
    return _with_tinkoff_response


def test_properly_unpack_session_info(controller_factory):
    controller = controller_factory({
        'resultCode': 'OK',
        'payload': 'TEST_SESSION_ID',
        'trackingId': 'TEST',
    })

    assert controller.get_initial_session_id() == 'TEST_SESSION_ID'


def test_sign_rejected_by_tinkoff(controller_factory):
    controller = controller_factory({
        'resultCode': 'OPERATION_REJECTED',
        'errorMessage': 'TEST - Операция недоступна',
        'plainMessage': 'Операция недоступна', 'trackingId': 'TEST_ID',
    })

    with pytest.raises(ImproperlySignedUpException):
        controller.sign_up('some_session_id')


def test_sign_up_works_fine(controller_factory):
    controller = controller_factory({
        'resultCode': 'OK',
        'payload': {
            'sessionid': 'singed-up-session-id',
            'accessLevel': 'CANDIDATE',
            'sessionTimeout': 600,
            'sessionId': 'test-session-id',
            'userId': '100500',
            'newUser': False,
        },
        'trackingId': 'test-tracking-id',
    })

    controller.sign_up('initial-session-id') == 'singed-up-session-id'


def test_make_level_up_works_raises_exception_when_tinkoff_is_down(controller_factory):
    controller = controller_factory({
        'resultCode': 'ERROR',
        'errorMessage': 'Error',
    })

    with pytest.raises(ImproperlySignedUpException):
        controller.make_level_up('signed-up-session')
