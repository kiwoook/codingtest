import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (k + 1)
# 코인 개수만큼 하나씩은 채워넣는다.


dp[0] = 1

for i in range(n):
    for j in range(coin_list[i], k+1):
        dp[j] += dp[j - coin_list[i]]

print(dp[k])
