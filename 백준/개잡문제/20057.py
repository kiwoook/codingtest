import sys
sys.setrecursionlimit(250000)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def rotate_90(list_value):
    return [list(row) for row in zip(*list_value[::-1])]


wind_board1 = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0],
]

wind_board2 = rotate_90(wind_board1)
wind_board3 = rotate_90(wind_board2)
wind_board4 = rotate_90(wind_board3)


def dfs(y, x, direction):
    global answer

    if visited[y][x] == 1:
        return

    visited[y][x] = 1
    ny = y + dy[direction]
    nx = x + dx[direction]

    if not (0 <= ny < n and 0 <= nx < n) or visited[ny][nx] == 1:
        direction = (direction + 1) % 4
        ny = y + dy[direction]
        nx = x + dx[direction]

    dfs(ny, nx, direction)

    if board[y][x] > 0:
        left = board[y][x]

        r_direction = (direction + 2) % 4
        tmp_wind = wind[direction]

        for i in range(5):
            for k in range(5):
                if tmp_wind[i][k] > 0:
                    sand = int(tmp_wind[i][k] * board[y][x])
                    left -= sand
                    if 0 <= y + i - 2 < n and 0 <= x + k - 2 < n:
                        board[y + i - 2][x + k - 2] += sand
                    else:
                        answer += sand

        if 0 <= y + dy[r_direction] < n and 0 <= x + dx[r_direction] < n:
            board[y + dy[r_direction]][x + dx[r_direction]] += left
        else:
            answer += left

        board[y][x] = 0


n = int(sys.stdin.readline().rstrip())
board = []
visited = [[0] * n for _ in range(n)]
answer = 0

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 회전 배열 넣기
wind = [wind_board1, wind_board2, wind_board3, wind_board4]

dfs(0, 0, 0)

print(answer)