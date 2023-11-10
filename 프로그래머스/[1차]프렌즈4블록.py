def solution(m, n, board):
    answer = 0
    for idx, v in enumerate(board):
        board[idx] = list(v)

    while 1:
        delete_pos = set()
        for i in range(m - 1):
            for k in range(n - 1):
                if board[i][k] == board[i + 1][k] == board[i][k + 1] == board[i + 1][k + 1] and board[i][k] != ' ':
                    delete_pos.add((i, k))
                    delete_pos.add((i + 1, k))
                    delete_pos.add((i, k + 1))
                    delete_pos.add((i + 1, k + 1))

        if len(delete_pos) == 0:
            break

        for y, x in delete_pos:
            if board[y][x] != ' ':
                board[y][x] = ' '
                answer += 1

        for i in range(m - 1, 0, -1):
            for k in range(n):
                if board[i][k] == ' ':
                    for j in range(i - 1, -1, -1):
                        if board[j][k] != ' ':
                            board[i][k], board[j][k] = board[j][k], board[i][k]
                            break

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
