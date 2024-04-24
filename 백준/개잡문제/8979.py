import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

rank_list = list()

d_dict = dict()
for _ in range(n):
    tmp_list = (list(map(int, sys.stdin.readline().rstrip().split())))
    d_dict[tmp_list[0]] = tuple(tmp_list[1:])
    rank_list.append(tuple(tmp_list[1:]))

rank_list.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

find_score = d_dict[k]
for rank_idx, value in enumerate(rank_list):
    if value == find_score:
        print(rank_idx + 1)
        break


