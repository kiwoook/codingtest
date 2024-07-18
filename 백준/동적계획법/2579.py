import sys

n = int(sys.stdin.readline().rstrip())
stair = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 초기 계단 수가 적은 경우를 처리
if n == 1:
    print(stair[0])
    exit(0)
elif n == 2:
    print(max(stair[0] + stair[1], stair[1]))
    exit(0)

# DP 배열 초기화
dp = [0] * n

# 초기값 설정
dp[0] = stair[0]
dp[1] = max(stair[0] + stair[1], stair[1])
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

# DP를 사용하여 최대 점수를 계산
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[n - 1])
