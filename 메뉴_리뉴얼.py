from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []

    for idx, order in enumerate(orders):
        orders[idx] = set(list(order))

    for c in course:
        comb = []
        for order in orders:
            comb.append(list(combinations(order,c)))
        comb = set(sum(comb, []))
        cnt_dict = defaultdict(list)
        for k in comb:
            cnt = 0
            k = set(k)
            for order in orders:
                if order >= k:
                    cnt += 1
            if cnt >= 2:
                cnt_dict[cnt].append(''.join(sorted(k)))
        if cnt_dict:
            max_value = max(cnt_dict.keys())
            answer.append(cnt_dict[max_value])

    answer = sorted(list(set(sum(answer, []))))

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
