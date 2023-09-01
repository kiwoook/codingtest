def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10
        if 0 < n < 5:
            answer += n
            storey -= n
        if n == 5:
            x = storey // 10 % 10
            if x >= 5:
                answer += 10 - n
                storey += 10 - n
            if 0 <= x < 5:
                answer += n
                storey -= n
        if 5 < n <= 9:
            answer += 10 - n
            storey += 10 - n
        storey //= 10

    return answer


print(solution(545))

