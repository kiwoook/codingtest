n = int(input())
dp = [0 for _ in range(91)]

dp[0] = 0
dp[1] = 1

for i in range(n - 1):
    dp[i + 2] = dp[i] + dp[i + 1]

print(dp[n])
