import sys

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i] = [dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n][0], dp[n][1])
