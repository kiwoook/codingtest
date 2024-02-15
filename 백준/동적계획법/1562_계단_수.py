n = int(input())

dp = [0 for _ in range(101)]

dp[1] = 9
dp[2] = 17

for i in range(2, 100):
    dp[i + 1] = (dp[i] - 2) * 2 + 2
    dp[i + 1] %= 1000000000


print(dp[n])
