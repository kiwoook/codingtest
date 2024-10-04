import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
max_value = 0
cnt_dict = defaultdict(int)

for _ in range(n):
    v = sys.stdin.readline().rstrip()
    cnt_dict[v] += 1
    if cnt_dict[v] > max_value:
        max_value = cnt_dict[v]

dict_list = sorted(list(cnt_dict.items()), key=lambda x: (-x[1], x[0]))

print(dict_list[0][0])
