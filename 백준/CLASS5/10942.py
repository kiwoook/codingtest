import sys

n = int(sys.stdin.readline().rstrip())
board = list(map(int, sys.stdin.readline().rstrip().split()))

# DP 동작
dp = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if board[i] == board[i+1]:
        dp[i][i + 1] = True

for step in range(2, n):
    for i in range(0, n):
        if i + step < n:
            dp[i][i + step] = (board[i] == board[i + step]) and dp[i + 1][i + step - 1]

m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    if dp[s - 1][e - 1]:
        print("1")
    else:
        print("0")
