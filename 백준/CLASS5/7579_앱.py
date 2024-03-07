import sys
arr = [0]
crr = [0]
n, m = map(int, sys.stdin.readline().rstrip().split())
arr.extend(list(map(int, sys.stdin.readline().rstrip().split())))
crr.extend(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 for _ in range(sum(crr) + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for max_cost in range(sum(crr) + 1):
        now_memory = arr[i]
        now_cost = crr[i]

        if max_cost < now_cost:
            dp[i][max_cost] = dp[i - 1][max_cost]
        else:
            dp[i][max_cost] = max(dp[i - 1][max_cost], now_memory + dp[i - 1][max_cost - now_cost])

min_value = int(1e9)

for i in range(1, n+1):
    for j in range(sum(crr) + 1):
        if dp[i][j] >= m:
            min_value = min(j, min_value)

print(min_value)
