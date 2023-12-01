import sys

n = int(input())
stair = []
for i in range(n):
    stair.append(int(sys.stdin.readline().rstrip()))

print(stair)

dp = [[0 for _ in range(2)] for _ in range(n)]

dp[0][0] = stair[0]
dp[0][1] = stair[1]

for i in range(n):
    for k in range(2):
        pass
