def solution(triangle):
    h = len(triangle)

    for i in range(h - 2, -1, -1):
        for k in range(0, i + 1):
            triangle[i][k] = triangle[i][k] + triangle[i + 1][k] if triangle[i][k] + triangle[i + 1][k] > triangle[i][
                k] + triangle[i + 1][k + 1] else triangle[i][k] + triangle[i + 1][k + 1]

    return triangle[0][0]


