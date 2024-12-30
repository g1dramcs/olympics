from random import randint

n = int(input("Кол-во строк: "))
m = int(input("Кол-во столбцов: "))
r = int(input("Макс. число рандом: "))

a = [[randint(0, r) for _ in range(m)] for _ in range(n)]
b = [[randint(0, r) for _ in range(m)] for _ in range(n)]
c = []

# Вывод массивов
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end='')
    print()
print("-------------")
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        print(b[i][j], end='')
    print()
    
# Умножение
for i in range(0, n):
    # Умножение и сложение через a[i][j] * b [i][j]
    c.append([])
    for j in range(0, m):
        # Диагональ 1:1 2:2 ...