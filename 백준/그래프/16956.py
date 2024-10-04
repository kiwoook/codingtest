import sys

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, sys.stdin.readline().rstrip().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

# S의 위치를 파악한 후 바로 옆에 W가 있지 않으면 울타리 설치

sheep_list = []

for i in range(r):
    for k in range(c):
        if board[i][k] == 'S':
            sheep_list.append((i, k))

print(sheep_list)

for y, x in sheep_list:
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if board[ny][nx] == 'W':
                print(0)
                exit(0)
            elif board[ny][nx] == '.':
                board[ny][nx] = 'D'

print(1)
for i in range(r):
    print(''.join(board[i]))
