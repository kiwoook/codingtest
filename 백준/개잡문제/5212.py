import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, sys.stdin.readline().rstrip().split())
board = []

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

cnt_board = [[0 for _ in range(c)] for _ in range(r)]

min_y, max_y = len(board), 0
min_x, max_x = len(board[0]), 0

for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if board[ny][nx] == '.':
                        cnt_board[y][x] += 1
                else:
                    cnt_board[y][x] += 1

for y in range(r):
    for x in range(c):
        if cnt_board[y][x] >= 3:
            board[y][x] = '.'

for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            min_x = min(min_x, x)
            max_x = max(max_x, x)

board = board[min_y:max_y + 1]
for i in range(len(board)):
    board[i] = board[i][min_x:max_x + 1]

for i in range(len(board)):
    print(''.join(board[i]))
