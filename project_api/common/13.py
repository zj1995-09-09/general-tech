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


"""输入某年某月某日，判断这一天是这一年的第几天,输入描述:
输入三行，分别是年，月，日
输出描述:
成功:返回outDay输出计算后的第几天;
                                           失败:返回-1 用 Python 求解"""