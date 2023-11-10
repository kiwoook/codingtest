# 시간 초과
max_value = 0
hap = 0


def dfs(depth, branch, n, triangle):
    global max_value, hap
    if depth == n:
        if max_value < hap:
            max_value = hap
        return

    hap += triangle[depth][branch]
    dfs(depth + 1, branch, n, triangle)
    dfs(depth + 1, branch + 1, n, triangle)
    hap -= triangle[depth][branch]


def solution(triangle):
    n = len(triangle)

    dfs(0, 0, n, triangle)

    return max_value


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
