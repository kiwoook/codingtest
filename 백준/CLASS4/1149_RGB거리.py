import sys

n = int(input())
rgb = []
dp = [[0 for _ in range(3)] for _ in range(n)]

for _ in range(n):
    rgb.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, n):
    for k in range(3):
        tmp = []
        for j in range(3):
            if k == j:
                continue
            tmp.append(dp[i-1][j])
        dp[i][k] = rgb[i][k] + min(tmp)

print(min(dp[n - 1]))
