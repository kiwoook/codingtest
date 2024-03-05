import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
idx_list = [(0, 0)]

for i in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    idx_list.append((w, v))

for i in range(1, n + 1):
    for max_weight in range(1, k + 1):
        now_weight, now_value = idx_list[i]

        if max_weight < now_weight:
            dp[i][max_weight] = dp[i - 1][max_weight]
        else:
            dp[i][max_weight] = max(dp[i - 1][max_weight], now_value + dp[i - 1][max_weight - now_weight])

print(dp[n][k])
