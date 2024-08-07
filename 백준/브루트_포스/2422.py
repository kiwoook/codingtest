import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
not_combine_dict = dict()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    not_combine_dict[tuple((a, b))] = 1
    not_combine_dict[tuple((b, a))] = 1

comb_list = list(combinations([i for i in range(1, n + 1)], 3))

answer = 0

for comb in comb_list:

    if not_combine_dict.get(tuple((comb[0], comb[1]))) is None and not_combine_dict.get(
            tuple((comb[0], comb[2]))) is None and not_combine_dict.get(tuple((comb[1], comb[2]))) is None:
        answer += 1

print(answer)
