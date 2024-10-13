# 15 зарплата. Посчитать через сколько дней зарплата


from datetime import timedelta, datetime

day = int(input())
month = int(input())
year = int(input())
day_in_month = [30, 31, 28, 29]

input_time = datetime(
    year,
    month,
    day,
)

# Проверка на високосный код
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)


print(input_time)
print(is_leap(year))