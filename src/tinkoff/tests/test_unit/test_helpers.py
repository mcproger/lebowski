from __future__ import annotations

from datetime import datetime, timezone

import pytest

from tinkoff.helpers import operations_piechar_url


@pytest.mark.freeze_time(datetime(2020, 1, 28, tzinfo=timezone.utc))
@pytest.mark.parametrize(
    ('from_datetime', 'to_datetime', 'expected_result'),
    [
        (
            None,
            None,
            'https://www.tinkoff.ru/api/common/v1/operations_piechart?end=1580169600000&'
            'groupBy=spendingCategory&notInner=true&start=1577836800000&type=Debit'
            '&sessionid=test-session&wuid=af3b1c996a3e2678fb05a25fab603e17',
        ),
        (
            datetime(2021, 1, 1, tzinfo=timezone.utc),
            datetime(2021, 4, 1, tzinfo=timezone.utc),
            'https://www.tinkoff.ru/api/common/v1/operations_piechart?end=1617235200000&'
            'groupBy=spendingCategory&notInner=true&start=1609459200000&type=Debit'
            '&sessionid=test-session&wuid=af3b1c996a3e2678fb05a25fab603e17',
        ),
    ],
)
def test_operations_piechart_url(from_datetime, to_datetime, expected_result):
    assert operations_piechar_url('test-session', from_datetime, to_datetime) == expected_result
