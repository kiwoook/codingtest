import sys
from collections import deque

INF = 1e12

n, m, t = map(int, sys.stdin.readline().rstrip().split())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

knife_y, knife_x = -1, -1

# 칼 위치
for i in range(n):
    for k in range(m):
        if board[i][k] == 2:
            knife_y, knife_x = i, k


def bfs(start_y, start_x, target_y, target_x, can_break_walls):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([(start_y, start_x, 0)])
    visited[start_y][start_x] = 1

    while q:
        y, x, time = q.popleft()

        if y == target_y and x == target_x:
            return time

        if time >= t:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if board[ny][nx] != 1 or can_break_walls:
                    visited[ny][nx] = 1
                    q.append((ny, nx, time + 1))

    return INF


# 1. 칼 없이 가는 루트
min_time_without_knife = bfs(0, 0, n - 1, m - 1, False)

# 2. 칼을 찾고 난 후, 칼을 사용하여 가는 루트
min_time_with_knife = INF
time_to_knife = bfs(0, 0, knife_y, knife_x, False)

if time_to_knife < INF:
    time_from_knife_to_end = bfs(knife_y, knife_x, n - 1, m - 1, True)
    min_time_with_knife = time_to_knife + time_from_knife_to_end

answer = min(min_time_without_knife, min_time_with_knife)
print(answer if answer <= t else "Fail")
