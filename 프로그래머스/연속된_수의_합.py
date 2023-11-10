def solution(num, total):
    start = num if num > total else total

    for i in range(-start, total + 1):
        answer = []
        total_sum = 0
        for k in range(i, i + num):
            total_sum += k
            answer.append(k)
        print(answer)
        if total_sum == total:
            return answer

    return [0]


print(solution(5, 0))
