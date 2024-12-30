# Написать программу которая находт наибольшее целое число, сумма четных положительных цифр которого кратна 3, в диапазоне от M до N включительно

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_largest_number(N, M):
    for num in range(N, M, -1):
        if sum_of_digits(num) % 4 == 0:
            if num % 2 == 0:
                return num
            else:
                continue
    return 0


M = int(input("M:"))
N = int(input("N:"))
print(find_largest_number(N, M))