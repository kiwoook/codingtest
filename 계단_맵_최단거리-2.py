def solution(maps):
    # BFS는 최단거리로 진입한다.

    n, m = len(maps), len(maps[0])
    queue = [(0, 0)]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
