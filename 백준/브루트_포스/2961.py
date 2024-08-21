import sys
from itertools import combinations

answer = int(1e12)
n = int(sys.stdin.readline().rstrip())
taste_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for choice in range(1, n + 1):
    comb_list = list(combinations([i for i in range(n)], choice))
    for comb in comb_list:
        sourness = 1
        bitterness = 0
        for idx in comb:
            sourness *= taste_list[idx][0]
            bitterness += taste_list[idx][1]

        answer = min(answer, abs(sourness - bitterness))

print(answer)
