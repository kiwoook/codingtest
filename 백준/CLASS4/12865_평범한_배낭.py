import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

a = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    a.append((w, v))

dp = [0 for _ in range(n)]
weight = 0

for i in range(n):
    weight += a[i][0]
    dp[i] = a[i][0]
    if weight > k:
        dp[i] -= weight - k
        break

print(dp)
