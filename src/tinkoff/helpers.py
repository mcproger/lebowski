from datetime import datetime

from tinkoff.constants import OPERATIONS_PIECHART_URL


def to_milliseconds(timestamp: int) -> int:
    return int(timestamp) * 1000


def operations_piechar_url(session: str, from_datetime: datetime = None, to_datetime: datetime = None) -> str:
    if from_datetime:
        from_timestamp = from_datetime.timestamp()
    else:
        from_timestamp = datetime.today().replace(day=1).timestamp()

    if to_datetime:
        to_timestamp = to_datetime.timestamp()
    else:
        to_timestamp = datetime.today().timestamp()

    return OPERATIONS_PIECHART_URL.format(
        signed_up_session_id=session, from_timestamp=to_milliseconds(from_timestamp),
        to_timestamp=to_milliseconds(to_timestamp),
    )


def convert_raw_tinkoff_data(raw_data: dict) -> dict:
    if not raw_data:
        return {}

    return {
        element['spendingCategory']['name']: element['amount']['value']
        for element in raw_data
    }
