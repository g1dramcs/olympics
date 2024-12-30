lst_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day, month, year, weekday = map(int, input().split())

if year%4==0 and (year%100!=0 or year%400==0):
    lst_month[1] + 1
    
summ = 0
count = 0
while count != month - 1:
    summ += lst_month[count]
    count += 1
summ += day - 1

print((summ + weekday) % 7) 