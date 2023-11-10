import sys

limit_number = 10000
sys.setrecursionlimit(limit_number)
path_map = []
hap = 0
n = 0
m = 0


def dfs(y, x, maps):
    global path_map, hap
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    hap += int(maps[y][x])

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] != 'X' and path_map[ny][nx] == 0:
                path_map[ny][nx] = 1
                dfs(ny, nx, maps)


def solution(maps):
    global path_map, hap, n, m
    answer = []
    n, m = len(maps), len(maps[0])
    path_map = [[0] * m for _ in range(n)]

    for idx, ms in enumerate(maps):
        maps[idx] = list(ms)

    for i in range(n):
        for k in range(m):
            if maps[i][k] != 'X' and path_map[i][k] == 0:
                path_map[i][k] = 1
                dfs(i, k, maps)
                answer.append(hap)
                hap = 0

    if not answer:
        return [-1]

    return sorted(answer)


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
