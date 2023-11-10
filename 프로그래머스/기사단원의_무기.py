import math


def count(num):
    cnt = 0

    for i in range(1, int(math.sqrt(num))+1):
        if i * i == num:
            cnt += 1
        elif num % i == 0:
            cnt += 2

    return cnt


def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        cnt = count(i)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer


print(solution(10, 3, 2))
