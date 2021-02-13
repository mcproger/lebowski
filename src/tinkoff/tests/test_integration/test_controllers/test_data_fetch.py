import pytest

from tinkoff.controllers.exceptions import InvalidOperationsPiecharRequest


def test_invalid_operations_piechar_response(statistic_controller_factory):
    controller = statistic_controller_factory({
        'resultCode': 'INVALID_REQUEST_DATA',
        'errorMessage': 'AUTTB15LL - Bad format. Parameter start. Invalid time format. UTC milliseconds is expected.',
        'plainMessage': 'Bad format. Parameter start. Invalid time format. UTC milliseconds is expected.',
        'trackingId': 'AUTTB15LL',
    })

    with pytest.raises(InvalidOperationsPiecharRequest):
        controller.get_operations_piechar('test-session')
