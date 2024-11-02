from random import random

n = int(input())
lst = []
lenght = []
count = 0
for i in range(n):
    lst.append(int(random() <= 0.8))
for i in lst:
    if i == 1:
        lenght.append(count)
    count += 1
print(f"самый длинный отрезок {max(lenght) - min(lenght)+ 1}")
print(lst)
