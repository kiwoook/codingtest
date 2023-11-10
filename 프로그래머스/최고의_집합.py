def solution(n, s):
    answer = []

    if n > s:
        return [-1]

    while n > 0:
        v = s // n
        answer.append(v)
        s -= v
        n -= 1
    return answer


print(solution(2, 9))
