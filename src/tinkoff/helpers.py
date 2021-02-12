from datetime import datetime

from tinkoff.constants import OPERATIONS_PIECHART_URL


def to_milliseconds(timestamp: int) -> int:
    return int(timestamp) * 1000


def operations_piechar_url(session: str, from_datetime: datetime = None, to_datetime: datetime = None) -> str:
    from_timestamp = from_datetime.timestamp() if from_datetime else datetime.today().replace(day=1).timestamp()
    to_timestamp = to_datetime.timestamp() if to_datetime else datetime.today().timestamp()

    return OPERATIONS_PIECHART_URL.format(
        signed_up_session_id=session, from_timestamp=to_milliseconds(from_timestamp),
        to_timestamp=to_milliseconds(to_timestamp),
    )