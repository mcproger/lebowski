from datetime import datetime
import pytest

from tinkoff.helpers import operations_piechar_url


@pytest.mark.freeze_time('2020-1-28')
@pytest.mark.parametrize(
    ('from_datetime', 'to_datetime', 'expected_result'),
    [
        (
            None, None,
            'https://www.tinkoff.ru/api/common/v1/operations_piechart?end=1580169600000&'
            'groupBy=spendingCategory&notInner=true&start=1577836800000&type=Debit'
            '&sessionid=test-session&wuid=af3b1c996a3e2678fb05a25fab603e17',
        ),
        (
            datetime(2021, 1, 1),
            datetime(2021, 4, 1),
            'https://www.tinkoff.ru/api/common/v1/operations_piechart?end=1617224400000&'
            'groupBy=spendingCategory&notInner=true&start=1609448400000&type=Debit'
            '&sessionid=test-session&wuid=af3b1c996a3e2678fb05a25fab603e17',
        ),
    ],
)
def test_operations_piechart_url(from_datetime, to_datetime, expected_result):
    assert operations_piechar_url('test-session', from_datetime, to_datetime) == expected_result