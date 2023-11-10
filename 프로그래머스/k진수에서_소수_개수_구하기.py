# 1. 진수 변환
# 2. 소수 찾기 단, 소수에는 0이 있으면 안됨

import math


def num_change(n, k):
    num = ""
    while n > 0:
        num = str(n % k) + num
        n = n // k
    return num


def solution(n, k):
    answer = []
    s = num_change(n, k)
    prime_chk_list = s.split("0")
    prime_chk_list = list(filter(None, prime_chk_list))

    prime_chk_list = list(map(int, prime_chk_list))

    for idx, p in enumerate(prime_chk_list):
        sw = 0
        if p == 1:
            continue
        for i in range(2, int(math.sqrt(p)) + 1):
            if p % i == 0:
                sw = 1
                break
        if sw == 0:
            answer.append(p)

    return len(answer)


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(883438, 3))
