from collections import defaultdict
from collections import Counter


def solution(X, Y):
    answer = ''
    x_dict, y_dict = dict(Counter(X)), dict(Counter(Y))
    x_set, y_set = set(x for x in x_dict.keys()), set(y for y in y_dict.keys())
    same = x_set & y_set
    if same == set():
        return "-1"
    if same == {'0'}:
        return "0"

    sorted_set = sorted(same)

    for value in sorted_set:
        if x_dict[value] > 0 and y_dict[value] > 0:
            if x_dict[value] < y_dict[value]:
                answer = value * x_dict[value] + answer
            else:
                answer = value * y_dict[value] + answer

    return answer


print(solution("00", "0"))
