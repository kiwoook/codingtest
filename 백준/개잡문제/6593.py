import sys
from collections import deque

dy = [0, 0, 0, 0, 1, -1]
dx = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

INF = int(1e12)

l, r, c = map(int, sys.stdin.readline().rstrip().split())

while l != 0 and r != 0 and c != 0:
    board = [[['0' for _ in range(c)] for _ in range(r)] for _ in range(l)]
    min_board = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    start = -1
    end = -1
    for i in range(l):
        for j in range(r):
            tmp = list(sys.stdin.readline().rstrip())
            for k in range(c):
                board[i][j][k] = tmp[k]
                if board[i][j][k] == 'S':
                    start = (i, j, k)
                if board[i][j][k] == 'E':
                    end = (i, j, k)
        tmp = sys.stdin.readline().rstrip()

    q = deque([start])
    sw = 0
    while q:
        z, y, x = q.popleft()

        if (z, y, x) == end:
            sw = 1
            break

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and min_board[nz][ny][nx] == 0 and (
                    board[nz][ny][nx] == '.' or board[nz][ny][nx] == 'E'):
                min_board[nz][ny][nx] = min_board[z][y][x] + 1
                q.append((nz, ny, nx))
    if sw == 0:
        print("Trapped!")
    else:
        print("Escaped in " + str(min_board[end[0]][end[1]][end[2]]) + " minute(s).")


    l, r, c = map(int, sys.stdin.readline().rstrip().split())
