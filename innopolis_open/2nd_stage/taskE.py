def max_mex(k, s, t, baskets):
    import sys
    from collections import defaultdict
    
    mex_values = []

    for i in range(k):
        if t == 1:
            ni, ci, numbers = baskets[i]
            count = defaultdict(int)
            for num in numbers:
                count[num] += 1
        else:  # t == 2
            ni, ci, numbers = baskets[i]
            count = defaultdict(int)
            for j in range(0, 2 * ni, 2):
                number = numbers[j]
                multiplicity = numbers[j + 1]
                count[number] += multiplicity

        # Now we can calculate the MEX for this basket
        available_increments = ci
        current_mex = 0

        while True:
            if available_increments > 0 or count[current_mex] > 0:
                if count[current_mex] > 0:
                    count[current_mex] -= 1
                else:
                    available_increments -= 1
                current_mex += 1
            else:
                break

        mex_values.append(current_mex)
    
    return max(mex_values)

# Reading the input
import sys
input = sys.stdin.read
data = input().splitlines()

k, s, t = map(int, data[0].split())
baskets = []

for i in range(1, 2 * k + 1, 2):
    ni, ci = map(int, data[i].split())
    numbers = list(map(int, data[i + 1].split())) if ni > 0 else []
    baskets.append((ni, ci, numbers))

# Calculating and printing the result
result = max_mex(k, s, t, baskets)
print(result)
