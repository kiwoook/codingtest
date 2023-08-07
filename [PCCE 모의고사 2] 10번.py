map_board = []


def check(board, pos):
    global map_board
    len_y_board = len(map_board)
    len_x_board = len(map_board[0])
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    [y, x] = pos
    cnt = 0
    for i in range(len(dy)):
        if 0 <= y + dy[i] < len_y_board and 0 <= x + dx[i] < len_x_board:
            if board[y + dy[i]][x + dx[i]] == 1:
                cnt += 1

    if board[y][x] == 1:
        if 2 >= cnt >= 5:
            return 0
        else:
            return 1
    else:
        if cnt == 2:
            return 1
        else:
            return 0


def solution(n, board, position):
    global map_board
    map_board = board
    answer = []
    print(map_board[5][3])
    for pos in position:
        answer.append(check(board, pos))

    return answer


print(
    solution(2, [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1]], [[1, 3], [5, 3]]))
