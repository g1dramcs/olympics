n, m = map(int, input().split())
alpha = float(input())
mod = 10**9 + 7
jobs = []
for i in range(n):
    l, r = map(int, input().split())
    jobs.append((l, r))

count = 0
for i in range(1 << n):
    selected_jobs = []
    total_max_time = 0
    total_min_time = 0
    for j in range(n):
        if (i >> j) & 1:
            selected_jobs.append(jobs[j])
            total_max_time += jobs[j][1]
            total_min_time += jobs[j][0]

    if total_max_time > m:
        continue

    valid = True
    remaining_time = m - total_min_time
    for j in range(n):
        if not ((i >> j) & 1):
            if remaining_time < jobs[j][1]:
                valid = False
                break
    if valid:
        count += 1

print(count % mod)

