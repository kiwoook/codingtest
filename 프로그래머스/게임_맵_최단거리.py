min_cnt = 1e9
map_list = []


def dfs(y, x, map_list, cnt, n, m):
    global min_cnt
    print(y, x)
    if y == n - 1 and x == m - 1:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
            if map_list[y + dy[i]][x + dx[i]] == 1:
                cnt += 1
                map_list[y][x] = 0
                dfs(y + dy[i], x + dx[i], map_list, cnt, n, m)
                map_list[y][x] = 1
                cnt -= 1


def solution_failed(maps):
    global min_cnt, map_list
    map_list = maps
    n = len(maps)
    m = len(maps[0])

    dfs(0, 0, map_list, 0, n, m)

    if min_cnt == 1e9:
        return -1

    return min_cnt + 1


def solution(maps):
    n, m = len(maps) - 1, len(maps[0]) - 1
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(0, 0)]

    while queue:
        y, x = queue.pop(0)
        print(y,x)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= m and 0 <= ny <= n and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    destination = maps[m][n]

    if destination == 1:
        return -1
    else:
        return destination



print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
