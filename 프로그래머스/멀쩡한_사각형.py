import math


def solution(w, h):
    # 로직은 맞는데 시간 복잡도에서 실패한 로직 ㅠ
    # 수학 못하니까 어쩔 수 없다...

    #     rectangle = w * h
    #     block = 0
    gcd = math.gcd(w, h)

    #     w = w // gcd
    #     h = h // gcd

    #     inclination = h / w
    #     previous_y = 0

    #     for x in range(1, w + 1):
    #         y = x * inclination
    #         diff = math.ceil(y) - math.floor(previous_y)
    #         block += diff
    #         previous_y = y

    return ((w // gcd) + (h // gcd) - 1) * gcd


print(solution(3, 2))
