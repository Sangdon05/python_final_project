from datetime import date, datetime

import pandas as pd

__logs = []


def write_log(isbn, is_rent, event_time=None):
    __logs.append((isbn, is_rent, event_time or datetime.now()))


def fetch_stats_with_pandas():
    # pandas 사용
    df = pd.DataFrame(__logs)
    rent_events = df[df[1] == True]

    # 월간 대여 통계
    # is_rent == True
    # log[2] -> 시간
    # 'monthly_rent_stats' = {'년-월-일': 횟수}

    sorted_count_monthly = tuple(
        rent_events.groupby(
            rent_events[2].astype(str)
        )  # YYYY-MM-DD 형식으로 변환하는 가장 빠른 방법
        .size()
        .sort_index(ascending=False)
        .items()
    )

    return sorted_count_monthly, int(rent_events[0].value_counts().idxmax())


def fetch_stats():
    if not __logs:
        return None, None

    # python 기본 기능 사용
    rent_events = [*filter(lambda x: x[1] == True, __logs)]

    # 월간 대여 통계
    # fliter is_rent == True
    # 시간을 년월일 문자열로 변환
    # dict에 추가하여 value를 횟수로하여 증가 시킨다.
    # 결과 [('년-월-일', 횟수)]

    dates = [*(x[2].strftime("%Y-%m-%d") for x in rent_events)]
    count_monthly = {}
    for x in set(dates):
        count_monthly.update({x: dates.count(x)})

    sorted_count_monthly = sorted(
        [*count_monthly.items()], key=lambda x: x[0], reverse=True
    )

    # 가장 많이 대여된 도서 통계
    # fliter is_rent == True
    # set(isbn)
    # list.count(isbn)
    # 결과 'best_rented_book' = int
    isbns = [*(x[0] for x in rent_events)]
    count_isbn = {}
    for x in set(isbns):
        count_isbn.update({x: isbns.count(x)})

    return sorted_count_monthly, max([*count_isbn.items()], key=lambda x: x[1])[0]


if __name__ == "__main__":
    write_log(123, True, date(2026, 8, 18))
    write_log(124, True, date(2026, 8, 18))
    write_log(125, True, date(2026, 8, 18))
    write_log(126, True, date(2026, 8, 18))
    write_log(127, False, date(2026, 8, 17))
    write_log(123, True, date(2026, 8, 17))
    write_log(129, True, date(2026, 8, 17))
    write_log(123, True, date(2026, 8, 17))
    write_log(143, False, date(2026, 8, 16))
    write_log(123, False, date(2026, 8, 16))
    write_log(123, True, date(2026, 8, 14))
    write_log(173, True, date(2026, 8, 13))

    print(fetch_stats())
    print(fetch_stats_with_pandas())
