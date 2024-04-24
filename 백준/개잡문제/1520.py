import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def dfs(y, x):
    global answer, dp

    if y == n - 1 and x == m - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    hap = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] < board[y][x]:
            hap += dfs(ny, nx)

    dp[y][x] = hap
    return dp[y][x]


n, m = map(int, sys.stdin.readline().rstrip().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[-1 for _ in range(m)] for _ in range(n)]

answer = 1

print(dfs(0, 0))


