from collections import defaultdict, deque

global_land = []
n = 0
m = 0


def bfs(i, k):
    cnt = 1

    # 초기값 지정 잘해두자.
    global_land[i][k] = 0
    q = deque([(i, k)])
    visited_x = {k}

    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if global_land[ny][nx] == 1:
                    cnt += 1
                    global_land[ny][nx] = 0
                    q.append((ny, nx))
                    visited_x.add(nx)

    return cnt, visited_x


def solution(land):
    global global_land, n, m
    global_land = land
    answer = 0
    n, m = len(land), len(land[0])
    x_dict = defaultdict(int)

    for i in range(n):
        for k in range(m):
            if global_land[i][k] == 1:
                cnt, visited_x = bfs(i, k)
                for x in visited_x:
                    x_dict[x] += cnt

    for v in x_dict.values():
        answer = max(v, answer)

    return answer


print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
