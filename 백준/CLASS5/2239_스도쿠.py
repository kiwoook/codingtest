import sys


def checking(y, x, value):
    for i in range(9):
        if board[y][i] == value or board[i][x] == value:
            return False

    # 3x3 영역 검사
    start_y = (y // 3) * 3
    start_x = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_y + i][start_x + j] == value:
                return False
    return True


def dfs(y, x):
    global board

    if y >= 9:
        # 모든 칸을 채웠을 때 출력
        for row in board:
            print(*row)
        exit(0)

    next_x = (x + 1) % 9
    next_y = y + 1 if next_x == 0 else y

    if board[y][x] == 0:
        for v in range(1, 10):
            if checking(y, x, v):
                board[y][x] = v
                dfs(next_y, next_x)
                board[y][x] = 0
    else:
        dfs(next_y, next_x)


board = []

for i in range(9):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(tmp)
# 백트래킹을 해야함
dfs(0, 0)
