import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    s = sys.stdin.readline().rstrip()
    cnt_dict = defaultdict(int)
    for v in s:
        if v == ' ':
            continue
        cnt_dict[v] += 1
    cnt = 0
    max_key = ''
    max_cnt = max(cnt_dict.values())

    for key, value in cnt_dict.items():
        if value == max_cnt:
            max_key = key
            cnt += 1

    if cnt > 1:
        print("?")
    else:
        print(max_key)
