def solution(n, m, section):
    answer = 0

    # 초기 세팅 구현
    lst = list(1 for i in range(n))
    for sec in section:
        lst[sec - 1] = 0

    # 색칠 놀이를 시작하자

    while sum(lst) != n:

        for sec in section:
            if lst[sec - 1] == 0:
                for i in range(sec - 1, sec + m - 1):
                    if i < n:
                        lst[i] = 1
                answer += 1
    return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
