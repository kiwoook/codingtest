import sys
from math import sqrt

INF = int(1e9)

n = int(sys.stdin.readline().rstrip())

dp = [INF for _ in range(50001)]

for idx in range(1, int(sqrt(n)) + 1):
    dp[idx * idx] = 1

for i in range(2, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[n])
