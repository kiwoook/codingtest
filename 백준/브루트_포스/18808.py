import sys

sw = 0


def add(y, x, sticker, board):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                board[y + i][x + j] = sticker[i][j]
    return board


def check(y, x, sticker, board):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if board[y + i][x + j] + sticker[i][j] == 2:
                return False
    return True


def rotate(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def dfs(depth, board):
    global sw
    if sw == 1:
        return

    if depth == k:
        sw = 1
        print(sum(sum(bd) for bd in board))
        return

    # 기존 상태를 장착시킬 수 있는 지 체크한다.
    sticker = arr_list[depth][:]
    for i in range(len(board) - len(sticker) + 1):
        for j in range(len(board[0]) - len(sticker[0]) + 1):
            if check(i, j, sticker, board):
                # 보드에 삽입한다.
                dfs(depth + 1, add(i, j, sticker, board))

    for i in range(3):
        sticker = rotate(sticker)
        for i in range(len(board) - len(sticker) + 1):
            for j in range(len(board[0]) - len(sticker[0]) + 1):
                if check(i, j, sticker, board):
                    # 보드에 삽입한다.
                    dfs(depth + 1, add(i, j, sticker, board))

    # 그래도 장착할 수 없다면 버리고 넘어간다
    dfs(depth + 1, board)


board_n, board_m, k = map(int, sys.stdin.readline().rstrip().split())
arr_list = []

for _ in range(k):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tmp_list = []
    for _ in range(n):
        tmp_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
    arr_list.append(tmp_list)

dfs(0, [[0] * board_m for _ in range(board_n)])
