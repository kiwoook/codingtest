def solution(n, a, b):
    answer = 0

    while a != b:
        a, b = (a - 1) // 2 + 1, (b - 1) // 2 + 1
        answer += 1

    return answer

print(solution( 8, 2, 3))