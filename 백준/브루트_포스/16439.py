import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
chicken_preference_list = []
answer = 0

for _ in range(n):
    chicken_preference_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

for a, b, c in list(combinations([i for i in range(m)], 3)):
    total = 0
    for person in chicken_preference_list:
        total += max(person[a], person[b], person[c])
    answer = max(answer, total)

print(answer)
