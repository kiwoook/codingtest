import sys
from collections import defaultdict

INF = 1e9


def min_suggest():
    min_list = []
    min_value = INF
    for key, value in suggest_dict.items():
        if min_value > value:
            min_value = value
            min_list = [key]
        elif min_value == value:
            min_list.append(key)

    old_order = INF
    old_key = 0

    for key in min_list:
        if order[key] < old_order:
            old_order = order[key]
            old_key = key

    order[old_key] = INF
    del suggest_dict[old_key]


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
suggest_list = list(map(int, sys.stdin.readline().rstrip().split()))
order = [INF for _ in range(m+1)]

suggest_dict = defaultdict(int)

for idx, suggest in enumerate(suggest_list):
    if order[suggest] == INF:
        order[suggest] = idx + 1

    if suggest in suggest_dict:
        suggest_dict[suggest] += 1
    elif len(suggest_dict) == n:
        min_suggest()
        suggest_dict[suggest] = 1
    else:
        suggest_dict[suggest] = 1

answer_list = sorted(suggest_dict.keys())

print(*answer_list)
