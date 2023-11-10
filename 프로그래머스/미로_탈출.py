from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    stack = deque()
    visited = [[0] * m for _ in range(n)]

    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    start_end_distance = 0
    end_y, end_x = 0, 0
    l_y, l_x = 0, 0

    for i in range(n):
        for k in range(m):
            if maps[i][k] == 'S':
                stack.append((i, k, start_end_distance))
                visited[i][k] = 1
            if maps[i][k] == 'E':
                end_y, end_x = i, k
            if maps[i][k] == 'L':
                l_y, l_x = i, k

    sw = 0
    while stack:
        y, x, start_end_distance = stack.popleft()
        print(y, x)
        if y == l_y and x == l_x:
            sw = 1
            visited = [[0] * m for _ in range(n)]
            stack.clear()
            stack.append((y, x, start_end_distance))
            visited[y][x] = 1
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                stack.append((ny, nx, start_end_distance + 1))
                visited[ny][nx] = 1
    if not sw:
        return -1
    sw = 0
    while stack:
        y, x, start_end_distance = stack.popleft()
        if y == end_y and x == end_x:
            sw = 1
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                stack.append((ny, nx, start_end_distance + 1))
                visited[ny][nx] = 1

    if not sw:
        return - 1

    return start_end_distance
