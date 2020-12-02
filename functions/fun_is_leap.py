month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 != 0)
    # return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


def day_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29

        return month_day[month]


print(is_leap(2000))
print(day_in_month(2020, 2))
