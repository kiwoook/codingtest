memo = {}


def w(a, b, c):
    global memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if (a, b, c) in memo:
        return memo[(a, b, c)]

    # 조건에 따른 계산
    if a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = w(20, 20, 20)
        return memo[(a, b, c)]

    if a < b < c:
        memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[(a, b, c)]

    # 위의 조건에 해당하지 않는 경우
    memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return memo[(a, b, c)]


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c)))
