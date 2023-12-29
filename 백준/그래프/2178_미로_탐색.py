import sys
from collections import deque

n, m = map(int, input().split())

board = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int,list(sys.stdin.readline().strip()))))

q = deque([(0, 0)])
visited[0][0] = 1

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

while q:
    y, x = q.popleft()
    if y == n - 1 and x == m - 1:
        print(board[y][x])
        break

    for j in range(4):
        ny = y + dy[j]
        nx = x + dx[j]

        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 0:
            if visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
                board[ny][nx] = board[y][x] + 1