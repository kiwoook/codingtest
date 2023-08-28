from collections import Counter
from collections import defaultdict


def solution(orders, course):
    answer = []

    total_order = []
    counting_dict = defaultdict(list)
    for order in orders:
        total_order.append(list(order))

    total_order = dict(Counter(sum(total_order, [])))

    print(total_order)

    for key, value in total_order.items():
        counting_dict[value].append(key)

    counting_dict = dict(counting_dict)

    counting_key = []
    for key in counting_dict.keys():
        counting_key.append(key)

    counting_key.sort()



    print(counting_dict)

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
