import copy
import sys


def dfs(y, x, board):
    global answer
    if y == n:
        cnt = sum(row.count(0) for row in board)
        answer = min(answer, cnt)
        return

    next_x = (x + 1) % m
    next_y = y + 1 if next_x == 0 else y

    # CCTV인 경우 처리
    if 0 < board[y][x] < 6:
        for direction_list in cctv_list[board[y][x]]:
            tmp_board = copy.deepcopy(board)

            for direction in direction_list:
                ny, nx = y, x
                while 0 <= ny < n and 0 <= nx < m:
                    if tmp_board[ny][nx] == 6:
                        break
                    if tmp_board[ny][nx] == 0:
                        tmp_board[ny][nx] = -1
                    ny += dy[direction]
                    nx += dx[direction]

            dfs(next_y, next_x, tmp_board)

    else:
        dfs(next_y, next_x, board)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

# CCTV 종류별 방향 목록
cctv_list = [
    [],  # 0은 사용 안 함
    [[0], [1], [2], [3]],  # CCTV 1번
    [[0, 1], [2, 3]],  # CCTV 2번
    [[0, 2], [0, 3], [1, 2], [1, 3]],  # CCTV 3번
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # CCTV 4번
    [[0, 1, 2, 3]]  # CCTV 5번
]

n, m = map(int, sys.stdin.readline().rstrip().split())
original_board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
answer = n * m

dfs(0, 0, original_board)

print(answer)
