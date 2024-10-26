from random import randint

index = 0
count = int(input())
lst = []
max_sums = []
best3_max_sums = []

for i in range(count):
    lst.append(randint(0, 100))

for i in lst:
    for l in lst:
        s = (i + l)
        if s % 7 == 0:
            max_sums.append(s)

print(lst)
print(max_sums)
if len(max_sums) <= 2:
    print("Числа не найдены")
else:
    while len(best3_max_sums) < 3:
        best3_max_sums.append(max(max_sums))
        max_sums.remove(max(max_sums))
        
print(best3_max_sums)
    