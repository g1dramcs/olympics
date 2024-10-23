from random import randint

index = 0
count = int(input())
lst = []
max_sums = []

for i in range(count):
    lst.append(randint(0, 100))

for i in lst:
    for l in lst:
        s = (i + l)
        if s % 5 == 0:
            max_sums.append(s)

print(lst)
print(max(max_sums))