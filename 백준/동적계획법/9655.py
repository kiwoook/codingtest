n = int(input())

dp = [-1 for _ in range(1001)]

dp[1] = True
dp[3] = True

for i in range(2, n + 1):
    if dp[i - 1] != -1:
        dp[i] = not dp[i - 1]
    elif i - 3 > 0 and dp[i - 3] != -1:
        dp[i] = not dp[i - 3]

print("SK" if dp[n] else "CY")
