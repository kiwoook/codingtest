import math


def solution(n, k):
    answer = []
    num = [i for i in range(1, n + 1)]
    factorial = math.factorial(n)

    for i in range(n, 0, -1):
        factorial //= i
        idx = (k-1) // factorial
        answer.append(num[idx])
        num.pop(idx)
        k = k % factorial

    return answer


print(solution(4, 6))
