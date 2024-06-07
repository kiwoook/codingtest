import sys

board = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

end_pos = n - 1

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

dy = [0, 1]
dx = [1, 0]

for y in range(n):
    for x in range(n):
        if y == n - 1 and x == n - 1:
            continue

        for i in range(2):
            ny = y + dy[i] * board[y][x]
            nx = x + dx[i] * board[y][x]
            if 0 <= ny < n and 0 <= nx < n:
                dp[ny][nx] += dp[y][x]

print(dp[end_pos][end_pos])
