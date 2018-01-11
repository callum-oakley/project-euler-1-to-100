from datetime import date, timedelta

def countSundays(dateFrom, dateTo):
    d, sundays = dateFrom, 0
    while d < dateTo:
        if d.day == 1 and d.weekday() == 6:
            sundays += 1
        d += timedelta(1)
    return sundays

print(countSundays(date(1901, 1, 1), date(2000, 12, 31)))
