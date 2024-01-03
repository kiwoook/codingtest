from collections import deque


def bfs():
    global board

    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    while q:
        z,y,x = q.popleft()

        if board[z][y][x] == -1:
            continue

        for u in range(6):
            nz = z + dz[u]
            ny = y + dy[u]
            nx = x + dx[u]

            if 0 <= nz < h and 0 <= ny < m and 0<= nx < n and board[nz][ny][nx] == 0:
                board[nz][ny][nx] = board[z][y][x] + 1
                q.append((nz, ny, nx))


n, m, h = map(int, input().split())

board = [[] for _ in range(h)]
q = deque([])
max_value = 0

for i in range(h):
    for j in range(m):
        board[i].append(list(map(int, input().split())))

for i in range(h):
    for j in range(m):
        for k in range(n):
            if board[i][j][k] == 1:
                q.append((i, j, k))

bfs()

for i in range(h):
    for j in range(m):
        for k in range(n):
            if board[i][j][k] == 0:
                print("-1")
                exit(0)
            max_value = max(max_value, board[i][j][k])


print(max_value - 1)