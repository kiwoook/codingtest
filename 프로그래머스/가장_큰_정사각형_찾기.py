
def solution(board):
    if not board:
        return 0

    rows = len(board)
    cols = len(board[0])
    max_side = 0

    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_side = max(max_side, dp[i][j])

    print(dp)

    return max_side ** 2

print(solution([[1,1,1,0,0], [1,1,0,0,0]]))

