from collections import Counter


def solution(array):
    answer = []

    dict_cnt = dict(Counter(array))

    max_value = max(dict_cnt.values())

    for key, value in dict_cnt.items():
        if value == max_value:
            answer.append(key)

    if len(answer) > 1:
        return -1

    return answer[0]
