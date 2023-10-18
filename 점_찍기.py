import math


def solution(k, d):
    answer = 0
    x = 0

    while x <= d:
        y = abs(math.sqrt(d ** 2 - x ** 2))
        answer += int((y // k) + 1)
        x += k

    return answer


print(solution(2, 4))
