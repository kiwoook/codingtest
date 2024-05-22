import sys
from collections import deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(y, x):
    # 여기서 나올 수 있는 최솟값 중 최대값이
    tmp_board = [[bd for bd in bord] for bord in board]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(y, x)])
    value = int(1e12)
    while q:
        y, x = q.popleft()

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                tmp_board[ny][nx] = tmp_board[y][x] + 1
                q.append((ny, nx))

    for ny, nx in shark_pos:
        value = min(value, tmp_board[ny][nx])

    return value


board = []
n, m = map(int, sys.stdin.readline().rstrip().split())
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

shark_pos = []
answer = 0

for i in range(n):
    for k in range(m):
        if board[i][k] == 1:
            shark_pos.append((i, k))

for i in range(n):
    for k in range(m):
        if board[i][k] == 0:
            answer = max(answer, bfs(i, k))

print(answer)
