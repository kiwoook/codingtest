import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(y, x):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(y, x)])
    visited[y][x] = 1
    max_len = 0

    while q:
        y, x = q.popleft()

        for u in range(4):
            ny = y + dy[u]
            nx = x + dx[u]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and board[ny][nx] == 'L':
                visited[ny][nx] = visited[y][x] + 1
                max_len = max(max_len, visited[ny][nx])
                q.append((ny, nx))

    return max_len - 1


board = []

n, m = map(int, sys.stdin.readline().rstrip().split())
answer = 0
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
    for k in range(m):
        if board[i][k] == 'L':
            answer = max(answer, bfs(i, k))

print(answer)
