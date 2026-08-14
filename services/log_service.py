from datetime import datetime

import pandas as pd

__logs = []


def write_log(isbn, is_rent):
    __logs.append((isbn, is_rent, datetime.now()))


def fetch_stats():
    # pandas 사용

    # 월간 대여 통계
    # is_rent == true
    # log[2] -> 시간

    # 가장 많이 대여된 도서 통계
    # count?
    pass


if __name__ == "__main__":
    write_log(123, True)
    write_log(124, True)
    write_log(125, True)
    write_log(126, True)
    write_log(127, False)
    write_log(123, True)
    write_log(129, True)
    write_log(123, True)
    write_log(143, False)
    write_log(123, False)
    write_log(123, True)
    write_log(173, True)

    df = pd.DataFrame(__logs)
    rent_logs = df[df[1] == True]
    print(rent_logs.value_counts(0))
    print(df.groupby(rent_logs[2].dt.date).size())
