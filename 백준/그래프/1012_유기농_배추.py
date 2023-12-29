import sys
from collections import deque


def bfs(i, k, m, n):
    global board, visited
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    q = deque([(i, k)])

    while q:
        y, x = q.popleft()
        board[y][x] = '1'

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                if visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        board[y][x] = 1

    cnt = 0

    for i in range(n):
        for k in range(m):
            if board[i][k] == 1:
                cnt += 1
                bfs(i, k, m, n)

    print(cnt)
