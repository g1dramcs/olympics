n = input("Введите число")
s = int(input("Введите систему счисления"))
lst = list(n)
c = len(lst)
dec_lst = []
for i in lst:
    c = c - 1
    dec_lst.append(int(i)*(s**c))

print("Результат:", sum(dec_lst))