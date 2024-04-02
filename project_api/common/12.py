def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def day_of_year(year, month, day):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_of_month[1] = 29
    return sum(days_of_month[:month - 1]) + day


try:
    year = int(input())
    month = int(input())
    day = int(input())
    outDay = day_of_year(year, month, day)
    print(outDay)
except:
    print(-1)
