from itertools import permutations

n, q = map(int, input().split())
a = list(map(int, input().split()))

queries = [int(input()) for _ in range(q)]

def check(arr, x):
    if len(arr) == 1:
        return arr[0] % x == 0
    
    results = set()
    for p in permutations(arr):
        new_arr = []
        for i in range(len(p) - 1):
            new_arr.append(p[i] ** p[i+1])
        results.add(check(list(new_arr),x))
    return True in results


for x in queries:
    if check(a, x):
        print("Yes")
    else:
        print("No")


