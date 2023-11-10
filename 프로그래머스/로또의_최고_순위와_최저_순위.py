def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        if lotto == 0:
            zero_cnt += 1

    answer.append(rank[cnt+zero_cnt])
    answer.append(rank[cnt])

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
