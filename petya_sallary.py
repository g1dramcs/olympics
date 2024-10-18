from datetime import datetime

list_days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(input())
month = int(input())
year = int(input())

def check_month():
    if day > 15:
        return month + 1
    else:
        return month

def check_year():
    if month == 12:
        return year + 1
    else:
        return year

time_sallary = datetime(
    check_year(),
    check_month(),
    15
)

if year%4==0 and (year%100!=0 or year%400==0):
    list_days_in_months[2] + 1
    
if day > 15:
    res = list_days_in_months[month -1] - day + 15
else:
    res = 15 - day
    

print(res)
print(time_sallary.isoweekday())