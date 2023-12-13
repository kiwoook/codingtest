import sys
def sum_of_submatrices(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # 누적합 배열 생성
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

    # 각 지점까지의 누적합 계산
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + matrix[i - 1][
                j - 1]

    # k 크기의 정사각형으로 배열 자르기
    for i in range(rows - k + 1):
        for j in range(cols - k + 1):
            total_sum = prefix_sum[i + k][j + k] - prefix_sum[i + k][j] - prefix_sum[i][j + k] + prefix_sum[i][j]
            result.append(total_sum)

    return result


min_value = 1e9

n, m, k = map(int, input().split())

board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

hap_board1 = [[0 for _ in range(m)] for _ in range(n)]
# BWBWBW 패턴
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if j % 2 == 0 and board[i][j] != 'B':
                hap_board1[i][j] = 1
            if j % 2 == 1 and board[i][j] != 'W':
                hap_board1[i][j] = 1

    if i % 2 == 1:
        for j in range(m):
            if j % 2 == 1 and board[i][j] != 'B':
                hap_board1[i][j] = 1
            if j % 2 == 0 and board[i][j] != 'W':
                hap_board1[i][j] = 1

hap_board2 = [[0 for _ in range(m)] for _ in range(n)]

# WBWBWB패턴
for i in range(n):
    if i % 2 == 1:
        for j in range(m):
            if j % 2 == 0 and board[i][j] != 'B':
                hap_board2[i][j] = 1
            if j % 2 == 1 and board[i][j] != 'W':
                hap_board2[i][j] = 1

    if i % 2 == 0:
        for j in range(m):
            if j % 2 == 1 and board[i][j] != 'B':
                hap_board2[i][j] = 1
            if j % 2 == 0 and board[i][j] != 'W':
                hap_board2[i][j] = 1

min_value1 = min(sum_of_submatrices(hap_board1, k))
min_value2 = min(sum_of_submatrices(hap_board2, k))

print(min(min_value1, min_value2))
