import sys
from collections import deque
from itertools import combinations

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
answer = int(1e9)


def distance(y1, x1, tmp_board):
    q = deque([(y1, x1)])
    visited = [[0 for _ in range(n)] for _ in range(n)]

    while q:
        y1, x1 = q.popleft()

        for j in range(4):
            ny = y1 + dy[j]
            nx = x1 + dx[j]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                tmp_board[ny][nx] = tmp_board[y1][x1] + 1
                q.append((ny, nx))
                visited[ny][nx] = 1

    return tmp_board


board = []
n, m = map(int, sys.stdin.readline().rstrip().split())

chiken_house_pos = list()
house_pos = []
house_board = [[0 for _ in range(n)] for _ in range(n)]
chiken_house_distance = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for k in range(n):
        if board[i][k] == 1:
            house_board[i][k] = 1
            house_pos.append((i, k))
        if board[i][k] == 2:
            chiken_house_pos.append((i, k))

for y, x in chiken_house_pos:
    tmp_board = [[h for h in house] for house in house_board]
    chiken_house_distance.append(distance(y, x, tmp_board))

# 치킨 하우스를 최대로 선택해야 한다.

comb_list = list(combinations([i for i in range(len(chiken_house_pos))], m))

for comb in comb_list:
    total_distance = 0
    for y, x in house_pos:
        tmp = []
        for c in comb:
            tmp.append(chiken_house_distance[c][y][x])
        total_distance += min(tmp)
    answer = min(answer, total_distance)

print(answer)
