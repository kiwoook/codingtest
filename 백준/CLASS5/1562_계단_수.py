def gadan(n):
    # n = int(sys.stdin.readline().rstrip())

    dp = [0 for _ in range(101)]

    dp[1] = 9
    dp[2] = 17

    for i in range(3, n + 1):
        dp[i] = ((dp[i - 1] - 2) * 2 + 2) % 1000000000

    return dp[n]


cnt = 0
for k in range(1, 41):
    cnt += gadan(k)

print(cnt)
