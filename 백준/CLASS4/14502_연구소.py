import copy
from collections import deque

max_cnt = 0


def bfs(map_list):
    cnt = 0

    q = deque([])

    for i in range(n):
        for k in range(m):
            if map_list[i][k] == 2:
                q.append((i, k))

    dy = [0, 0, 1, -1]
    dx = [-1, 1, 0, 0]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map_list[ny][nx] == 0:
                    map_list[ny][nx] = 2
                    q.append((ny, nx))

    for i in range(n):
        for k in range(m):
            if map_list[i][k] == 0:
                cnt += 1

    return cnt


def dfs(y, x, cnt):
    global board, max_cnt

    if cnt == 3:
        value = bfs(copy.deepcopy(board))
        if max_cnt < value:
            max_cnt = value
        return

    if board[y][x] == 0:
        board[y][x] = 1
        dfs(y, x, cnt + 1)
        board[y][x] = 0
    if x + 1 < m:
        dfs(y, x + 1, cnt)
    elif y + 1 < n:
        dfs(y + 1, 0, cnt)


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dfs(0, 0, 0)

print(max_cnt)
