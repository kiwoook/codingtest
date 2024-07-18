answer = 0

checking_list = [[(0, -1), (-1, -1), (-1, 0), (0, 0)], [(-1, 0), (-1, 1), (0, 1), (0, 0)],
                 [(0, 1), (1, 1), (1, 0), (0, 0)],
                 [(1, 0), (1, -1), (0, -1), (0, 0)]]


def dfs(y, x, sw):
    global answer, board

    # 만약 2*2가 판별되면 배치하지 않고 다음으로 넘긴다.
    if sw == 1:
        if (y >= 1 and x >= 1) and board[y - 1][x - 1] == board[y - 1][x] == board[y][x - 1] == 1:
            return

    if y == n - 1 and x == m - 1:
        answer += 1
        return

    next_x = x + 1
    next_y = y
    if next_x == m:
        next_x = 0
        next_y += 1

    board[next_y][next_x] = 1
    dfs(next_y, next_x, 1)
    board[next_y][next_x] = 0
    dfs(next_y, next_x, 0)


n, m = map(int, input().split())

board = [[0] * m for _ in range(n)]
board[0][0] = 1
dfs(0, 0, 1)
board[0][0] = 0
dfs(0, 0, 0)

print(answer)
