import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(n)]

for idx in range(0, n):
    dp[idx] = a[idx]
    hap = 0
    for check_idx in range(idx - 1, -1, -1):
        if a[idx] > a[check_idx]:
            hap = max(hap, dp[check_idx])
    dp[idx] += hap

print(max(dp))
