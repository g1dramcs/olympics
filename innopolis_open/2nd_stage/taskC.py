def to_ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))

def is_beautiful(n):
    ternary = to_ternary(n)
    return "1" not in ternary

n = int(input())
MOD = 998244353

beautiful_jumps = [i for i in range(n + 1) if is_beautiful(i)]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for jump in beautiful_jumps:
        if i - jump >= 0:
            dp[i] = (dp[i] + dp[i - jump]) % MOD

print(dp[n])
