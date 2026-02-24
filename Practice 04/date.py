# date.py
# Python date tasks

from datetime import datetime, date, timedelta

def subtract_five_days_from_today():
    today = date.today()
    result = today - timedelta(days=5)
    return today, result


def print_yesterday_today_tomorrow():
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow


def drop_microseconds(dt: datetime):
    return dt.replace(microsecond=0)


def date_diff_in_seconds(d1: datetime, d2: datetime) -> int:
    diff = d2 - d1
    return int(diff.total_seconds())


def main():
    # 1) subtract five days from current date
    today, minus5 = subtract_five_days_from_today()
    print("Today:", today)
    print("Today - 5 days:", minus5)

    # 2) yesterday, today, tomorrow
    y, t, tm = print_yesterday_today_tomorrow()
    print("\nYesterday:", y)
    print("Today:", t)
    print("Tomorrow:", tm)

    # 3) drop microseconds
    now = datetime.now()
    print("\nNow with microseconds:", now)
    print("Now without microseconds:", drop_microseconds(now))

    # 4) difference between two dates in seconds
    # input format: YYYY-MM-DD HH:MM:SS
    print("\nEnter two datetimes to calculate difference in seconds.")
    s1 = input("Datetime 1 (YYYY-MM-DD HH:MM:SS): ").strip()
    s2 = input("Datetime 2 (YYYY-MM-DD HH:MM:SS): ").strip()

    dt1 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")

    print("Difference in seconds:", date_diff_in_seconds(dt1, dt2))


if __name__ == "__main__":
    main()