from random import randint

index = 0
count = int(input())
lst = []
max_sum = 0

for i in range(count):
    lst.append(randint(0, 100))

for i in lst:
    for l in lst:
        print(i + l)
    