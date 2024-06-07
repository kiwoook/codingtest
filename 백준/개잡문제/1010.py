import sys

T = int(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(30)] for _ in range(30)]

# 초기화
for i in range(30):
    dp[i][i] = 1
    dp[i][0] = 1
for i in range(2, 30):
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for _ in range(T):
    n, k = map(int, sys.stdin.readline().rstrip().split())

    print(dp[k][n])
