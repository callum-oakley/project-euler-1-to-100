from datetime import date, timedelta


def main():
    d = date(1901, 1, 1)
    count = 0
    while d < date(2000, 12, 31):
        if d.day == 1 and d.weekday() == 6:
            count += 1
        d += timedelta(1)
    return count
    # 171
