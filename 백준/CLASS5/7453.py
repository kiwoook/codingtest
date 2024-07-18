import sys
from collections import defaultdict


def four_sum_count():
    ab_sum_count = defaultdict(int)
    for a in A:
        for b in B:
            ab_sum_count[a + b] += 1

    count = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in ab_sum_count:
                count += ab_sum_count[target]

    return count


n = int(sys.stdin.readline().rstrip())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

A = []
B = []
C = []
D = []

for bd in board:
    A.append(bd[0])
    B.append(bd[1])
    C.append(bd[2])
    D.append(bd[3])

result = four_sum_count()

print(result)
