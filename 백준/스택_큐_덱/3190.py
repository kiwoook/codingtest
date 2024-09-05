import sys
from collections import deque

answer = 0
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n = int(sys.stdin.readline().rstrip())
board = [[0] * n for _ in range(n)]
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    board[y - 1][x - 1] = 2

y, x, turn = 0, 0, 0
board[0][0] = 1

L = int(sys.stdin.readline().rstrip())
move_list = deque([sys.stdin.readline().rstrip().split() for _ in range(L)])
move_list.append([str(int(1e9)), None])
sw = False
visited_q = deque([(0, 0)])

while move_list:
    sec, change_turn = move_list.popleft()
    sec = int(sec)

    for _ in range(answer, sec):
        y += dy[turn]
        x += dx[turn]
        visited_q.append((y, x))
        answer += 1
        if not (0 <= y < n) or not (0 <= x < n) or board[y][x] == 1:
            print(answer)
            exit(0)
        elif board[y][x] == 2:
            board[y][x] = 1
        else:
            tail_y, tail_x = visited_q.popleft()
            board[tail_y][tail_x] = 0
            board[y][x] = 1

    if change_turn == 'D':
        turn = (turn - 1) % 4
    else:
        turn = (turn + 1) % 4
