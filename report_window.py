from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from config import REPORT_HOUR


JST = ZoneInfo("Asia/Tokyo")


def get_report_window(now=None):
    if now is None:
        now = datetime.now(JST)

    end = now.replace(hour=REPORT_HOUR, minute=0, second=0, microsecond=0)

    if now < end:
        end = end - timedelta(days=1)

    start = end - timedelta(days=1)

    return start, end


def is_in_report_window(published_datetime, start, end):
    if published_datetime is None:
        return False

    published_jst = published_datetime.astimezone(JST)

    return start <= published_jst < end
