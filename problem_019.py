from datetime import date, timedelta


def count_sundays(date_from, date_to):
    d, sundays = date_from, 0
    while d < date_to:
        if d.day == 1 and d.weekday() == 6:
            sundays += 1
        d += timedelta(1)
    return sundays


print(count_sundays(date(1901, 1, 1), date(2000, 12, 31)))
# 171
