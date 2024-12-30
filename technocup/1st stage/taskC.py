def count_divisors(n):
    if n == 1:
        return 1
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def count_beautiful_lengths(t, d):
    low = max(1, t - d)
    high = t + d
    beautiful_count = 0

    for length in range(low, high + 1):
        if count_divisors(length) <= 3:
            beautiful_count += 1
    
    return beautiful_count

# чтение входных данных
t, d = map(int, input().split())

# подсчет и вывод результата
print(count_beautiful_lengths(t, d))
