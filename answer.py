def find_closest(num1, direction):
    while True:
        divisions1 = 0
        num1 += direction
        for j in range(1, num1):
            if num1 % j == 0:
                divisions1 += 1
        if divisions1 == 1:
            break
    return num1


num = int(input("num:"))
divisions = 0
for i in range(1, num):
    if num % i == 0:
        divisions += 1
if divisions == 1:
    print('простое')
    simple = True
else:
    print('Не простое')
    simple = False

if not simple:
    min_num = find_closest(num, -1)
    max_num = find_closest(num, 1)
    if num - min_num > max_num - num:
        closest = max_num
    elif num - min_num < max_num - num:
        closest = min_num
    else:
        closest = [max_num, min_num]
    print('Ближайшее простое:', closest)
