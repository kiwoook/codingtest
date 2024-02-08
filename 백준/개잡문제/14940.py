import sys
from collections import deque


def bfs(a, b):
    global board, visited
    cnt = 1
    q = deque([(a, b)])
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    visited[a][b] = 1
    board[a][b] = 0
    while q:
        y, x = q.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 0 and visited[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))
                visited[ny][nx] = 1



n, m = map(int, input().split())
board = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

sw = 0

for i in range(n):
    for k in range(m):
        if board[i][k] == 2:
            bfs(i, k)
            sw = 1
            break
    if sw:
        break

for i in range(n):
    for k in range(m):
        if visited[i][k] == 0 and board[i][k] != 0:
            board[i][k] = -1

for i in range(n):
    print(*board[i])
