from collections import Counter


def solution(k, tangerine):
    answer = 0

    fruit_counter = dict(sorted(dict(Counter(tangerine)).items(), key=lambda x: x[1]))

    cnt = 0
    for fruit in fruit_counter.values():
        answer += 1
        cnt += fruit
        if fruit >= k:
            break

    return answer
