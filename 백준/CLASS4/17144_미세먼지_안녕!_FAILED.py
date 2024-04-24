import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def clean(a, b):
    # 위에 회전
    y, x = a, 1
    index = 1  # 우부터 시작
    temp = 0  # 공기청정기에서 나오는 바람
    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if ny == r or nx == c or ny == -1 or nx == -1:  # 벽에 닿았을 때
            index = (index - 1) % 4
            continue
        if y == a and x == 0:  # 공기청정기로 다시 돌아옴
            break
        board[y][x], temp = temp, board[y][x]  # swap
        y, x = ny, nx
    # 아래 회전
    y, x = b, 1
    index = 1  # 우부터 시작 우 하 좌 상
    temp = 0  # 공기청정기에서 나오는 바람
    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if nx == c or ny == r or ny == -1 or nx == -1:  # 벽에 닿았을 때
            index = (index + 1) % 4
            continue
        if y == b and x == 0:  # 공기청정기로 다시 돌아옴
            break
        board[y][x], temp = temp, board[y][x]  # swap
        y, x = ny, nx


r, c, t = map(int, sys.stdin.readline().rstrip().split())
board = []

visited = [[0 for _ in range(c)] for _ in range(r)]

for _ in range(r):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 미세먼지 위치 스캔

q = deque([])

air_q = []
sw = 0

# 에어 프레시
for i in range(r):
    for k in range(c):
        if board[i][k] > 0:
            q.append((i, k, board[i][k]))
        if board[i][k] == -1 and sw == 0:
            air_q.append((i, k))
            sw = 1

for _ in range(t):
    while q:
        y, x, value = q.popleft()
        cnt = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != -1:
                board[ny][nx] += value // 5
                cnt += 1
        board[y][x] -= cnt * (value // 5)

    for i in range(r):
        for k in range(c):
            if board[i][k] > 0:
                q.append((i, k, board[i][k]))

    clean(air_q[0][0], air_q[0][0] + 1)
    print("-----")
    for i in range(r):
        print(*board[i])
    print("----")

answer = 0
for i in range(r):
    for k in range(c):
        if board[i][k] > 0:
            answer += board[i][k]

print(answer)
