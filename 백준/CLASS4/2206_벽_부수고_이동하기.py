import sys
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

INF = int(1e9)
answer = INF


def find_wall(pos_y, pos_x):
    q = deque([(pos_y, pos_x)])
    wall_set = set()
    visited = dict()
    visited[(pos_y, pos_x)] = True
    while q:
        y, x = q.popleft()

        for z in range(4):
            ny = y + dy[z]
            nx = x + dx[z]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1:
                    wall_set.add((ny, nx))
                if not visited.get((ny, nx), False) and board[ny][nx] == 0:
                    visited[(ny, nx)] = True
                    q.append((ny, nx))

    return wall_set


def bfs(wall_y, wall_x):
    tmp_board[wall_y][wall_x] = 0
    tmp_board[0][0] = 1
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        if y == n - 1 and x == m - 1:
            return tmp_board[y][x]

        for z in range(4):
            ny = y + dy[z]
            nx = x + dx[z]
            if 0 <= ny < n and 0 <= nx < m and tmp_board[ny][nx] == 0:
                tmp_board[ny][nx] = tmp_board[y][x] + 1
                q.append((ny, nx))

    return INF


n, m = map(int, sys.stdin.readline().rstrip().split())
board = []

for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    tmp = list(map(int, tmp))
    board.append(tmp)

wall_list1 = find_wall(0, 0)


for w_y, w_x in wall_list1:
    tmp_board = [[b for b in bd] for bd in board]
    answer = min(answer, bfs(w_y, w_x))

# 벽돌 없이 그냥 가는 것도 탐색
answer = min(answer, bfs(0, 0))

if answer == INF:
    print(-1)
else:
    print(answer)
