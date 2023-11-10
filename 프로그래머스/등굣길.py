cnt = 0


def recur(x, y, puddles, m, n):
    print(x, y)
    global cnt

    for puddle in puddles:
        if [x, y] == puddle:
            return

    if x > m or y > n:
        return

    if x == m and y == n:
        cnt += 1
        return

    recur(x + 1, y, puddles, m, n)
    recur(x, y + 1, puddles, m, n)


def solution_failed(m, n, puddles):
    recur(1, 1, puddles, m, n)
    return cnt


def solution(m, n, puddles):
    road = [[0] * (m + 1) for _ in range(n + 1)]

    for [x, y] in puddles:
        road[y][x] = -1

    road[1][1] = 1

    dy = [-1, 0]
    dx = [0, -1]

    for i in range(1, n + 1):
        for k in range(1, m + 1):
            if i == 1 and k == 1 or road[i][k] == -1:
                continue
            for j in range(2):
                dn, dm = i + dy[j], k + dx[j]
                if dm <= m and dn <= n:
                    if road[dn][dm] == -1:
                        continue
                    road[i][k] += road[dn][dm]

    return road[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
