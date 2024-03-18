import sys


# 숫자가 같지 않으면 무의미


def down(board, cnt_board):
    pass


def up(board, cnt_board):
    pass


def left(board, cnt_board):
    pass


def right(board, cnt_board):
    pass


def dfs(depth, board):
    global max_value

    cnt_board = [[0 for _ in range(n)] for _ in range(n)]

    if depth == 5:
        max_value = max(max_value, max(board))


max_value = 0
original_board = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    original_board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# bd = [[org for org in org_board] for org_board in original_board]


dfs(0, original_board)
