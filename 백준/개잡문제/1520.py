import sys

sys.setrecursionlimit(10 ** 9)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def dfs(y, x):
    global dp

    if y == n - 1 and x == m - 1:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] < board[y][x]:
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]


n, m = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

print(dfs(0, 0))
