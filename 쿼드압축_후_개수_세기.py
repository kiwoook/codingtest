cnt_0 = 0
cnt_1 = 0


def divide(y, x, n, arr):
    global cnt_0, cnt_1
    if n == 0:
        return

    hap = 0
    for i in range(n):
        for k in range(n):
            hap += arr[y + i][x + k]

    if hap == 0:
        cnt_0 += 1
        return
    elif hap == n * n:
        cnt_1 += 1
        return

    else:
        divide(y, x, n // 2, arr)
        divide(y + (n // 2), x, n // 2, arr)
        divide(y, x + (n // 2), n // 2, arr)
        divide(y + (n // 2), x + (n // 2), n // 2, arr)


def solution(arr):
    n = len(arr)

    divide(0, 0, n, arr)

    return [cnt_0, cnt_1]


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
