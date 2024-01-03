from collections import deque


def bfs():
    global board, cnt

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()

        if board[y][x] == -1:
            continue

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))


n, m = map(int, input().split())

board = []
answer = []
max_value = 0
# 배열 두 개를 사용하면 메모리 초과가 발생할수도,,,
cnt = 0
q = deque([])

for _ in range(m):
    board.append(list(map(int, input().split())))

for i in range(m):
    for k in range(n):
        if board[i][k] == 1:
            q.append((i, k))

bfs()

for i in range(m):
    for k in range(n):
        if board[i][k] == 0:
            print("-1")
            exit(0)
        max_value = max(max_value, board[i][k])

print(max_value - 1)
