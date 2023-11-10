from math import factorial


def solution(n):
    answer = 0
    k = 0
    if n % 2 == 0:
        i = n // 2
    else:
        i = n // 2
        k = 1

    while i >= 0:
        answer += factorial(i + k) // (factorial(i) * factorial(k))
        i -= 1
        k += 2

    return answer % 1234567


print(solution(2000))
