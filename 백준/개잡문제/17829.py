# 배열을 계속 줄여서 한개로 만들어야함
import sys


def calculate_board(y, x, length):
    tmp_board = []

    if length == 2:
        sorted_list = sorted([board[y][x], board[y + 1][x], board[y][x + 1], board[y + 1][x + 1]])
        return sorted_list[-2]

    for i in range(0, length, 2):
        tmp = []
        for k in range(0, length, 2):
            tmp.append(calculate_board(i, k, 2))
        tmp_board.append(tmp)

    return tmp_board


n = int(sys.stdin.readline().rstrip())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

while type(board) is not int:
    board = calculate_board(0, 0, len(board))

print(board)
