import pytz
from datetime import datetime

from tinkoff.constants import OPERATIONS_PIECHART_URL


def to_milliseconds(timestamp: int) -> int:
    return int(timestamp) * 1000


def make_aware(datetime_obj: datetime) -> datetime:
    return datetime_obj.astimezone(pytz.utc)


def operations_piechar_url(session: str, from_datetime: datetime = None, to_datetime: datetime = None) -> str:
    if from_datetime:
        from_timestamp = make_aware(from_datetime).timestamp()
    else:
        from_timestamp = make_aware(datetime.today().replace(day=1)).timestamp()

    if to_datetime:
        to_timestamp = make_aware(to_datetime).timestamp()
    else:
        to_timestamp = make_aware(datetime.today()).timestamp()

    return OPERATIONS_PIECHART_URL.format(
        signed_up_session_id=session, from_timestamp=to_milliseconds(from_timestamp),
        to_timestamp=to_milliseconds(to_timestamp),
    )
