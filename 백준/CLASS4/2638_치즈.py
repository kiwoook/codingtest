import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def outside_air(pos_y, pos_x):
    global board
    visited = [[0 for _ in range(m)] for _ in range(n)]

    air_q = deque([(pos_y, pos_x)])
    board[pos_y][pos_x] = 2
    visited[pos_y][pos_x] = 1

    while air_q:
        y, x = air_q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and board[ny][nx] == 0:
                visited[ny][nx] = 1
                board[ny][nx] = 2
                air_q.append((ny, nx))


n, m = map(int, sys.stdin.readline().rstrip().split())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

outside_air(0, 0)

q = deque([])

for i in range(n):
    for k in range(m):
        if board[i][k] == 1:
            q.append((i, k))

answer = 0
while q:


    answer += 1
    tmp_q = deque([])
    remove_list = []
    while q:
        y, x = q.popleft()
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if board[ny][nx] == 2:
                cnt += 1
        if cnt >= 2:
            remove_list.append((y, x))
        else:
            tmp_q.append((y, x))

    for y, x in remove_list:
        board[y][x] = 0
        outside_air(y, x)

    q = tmp_q

print(answer)
