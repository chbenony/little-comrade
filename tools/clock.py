from datetime import datetime


def get_current_time():
    return datetime.now().astimezone().strftime(
        "%Y-%m-%d %I:%M:%S %p %Z (UTC%z)"
    )
