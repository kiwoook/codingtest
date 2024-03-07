# TODO 목요일에 하장
# 까먹을 수 있을까 쓰는 로직
# DP를 처음 돌릴 때 맨 처음 값을 저장해둔다.
# 저장해두다가 마지막 인덱스에 도착할 때 해당 스타트 값은 하지 않도록 로직을 구현하자.

import sys

rgb = [[0,0,0]]
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    rgb.append(list(map(int, sys.stdin.readline().rstrip().split())))


ans = int(1e12)

for start_idx in range(3):
    dp = [[0, 0, 0] for _ in range(n+1)]
    for i in range(3):
        if i == start_idx:
            dp[1][start_idx] = rgb[1][start_idx]
        else:
            dp[1][i] = int(1e12)
    for i in range(2, n+1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + rgb[i][2]
    for i in range(3):
        if i == start_idx:
            continue
        ans = min(ans, dp[n][i])

print(ans)
