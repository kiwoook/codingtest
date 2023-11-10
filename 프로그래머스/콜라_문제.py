def solution(a, b, n):
    answer = 0

    while n >= a:
        x = n // a
        n %= a
        n += x * b
        answer += x * b

    return answer


print(solution(2, 1, 20))
