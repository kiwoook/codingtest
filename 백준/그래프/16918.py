import sys
from collections import defaultdict

board = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c, n = map(int, input().split())

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))
bomb_dict = defaultdict(list)

for i in range(r):
    for k in range(c):
        if board[i][k] == 'O':
            bomb_dict[3].append((i, k))

time = 2

while time <= n:

    # 먼저 폭탄의 위치를 저장해둔다.
    if time % 2 == 0:
        board = [['O' for _ in range(c)] for _ in range(r)]

    if time % 2 == 1:
        if bomb_dict.get(time) is not None:
            while bomb_dict[time]:
                y, x = bomb_dict[time].pop()
                board[y][x] = '.'
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < r and 0 <= nx < c:
                        board[ny][nx] = '.'

        for i in range(r):
            for k in range(c):
                if board[i][k] == 'O':
                    bomb_dict[time + 2].append((i, k))

    time += 1

for i in range(r):
    print(''.join(board[i]))
