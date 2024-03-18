import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(y, x, value, visited):
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                if board[ny][nx] == value:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    return visited


def nomal():
    visited = [[0 for _ in range(n)] for _ in range(n)]

    cnt = 0

    for i in range(n):
        for k in range(n):
            if visited[i][k] == 0:
                visited = bfs(i, k, board[i][k], visited)
                cnt += 1

    return cnt


board = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

one = nomal()

for i in range(n):
    for k in range(n):
        if board[i][k] == 'G':
            board[i][k] = 'R'

two = nomal()

print(one, two)
