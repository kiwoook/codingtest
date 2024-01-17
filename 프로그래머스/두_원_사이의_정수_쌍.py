import math


def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        if x > r1:
            y2 = math.sqrt((r2 ** 2) - (x ** 2))
            answer += math.floor(y2) + 1
        else:
            y2 = math.sqrt((r2 ** 2) - (x ** 2))
            y1 = math.sqrt((r1 ** 2) - (x ** 2))
            answer += math.floor(y2) - math.ceil(y1) + 1

    return answer * 4


print(solution(2, 3))
