# 상향식으로 했는데...흠...재귀가 문제인듯...

max_hap = 0
hap = 0


def bottomUp(depth, branch, n, triangle):
    global hap, max_hap

    if depth == -1:
        if max_hap < hap:
            max_hap = hap
        return

    hap += triangle[depth][branch]

    if branch == 0:
        bottomUp(depth - 1, 0, n, triangle)
    elif branch == depth:
        bottomUp(depth - 1, branch - 1, n, triangle)
    else:
        if triangle[depth - 1][branch - 1] > triangle[depth - 1][branch]:
            bottomUp(depth - 1, branch - 1, n, triangle)
        elif triangle[depth - 1][branch - 1] < triangle[depth - 1][branch]:
            bottomUp(depth - 1, branch, n, triangle)
        else:
            bottomUp(depth - 1, branch - 1, n, triangle)
            bottomUp(depth - 1, branch, n, triangle)
    hap -= triangle[depth][branch]


def solution(triangle):
    n = len(triangle)

    for i in range(n):
        bottomUp(n - 1, i, n, triangle)

    return max_hap


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
