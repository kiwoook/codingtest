import sys
from collections import defaultdict

cnt_x = defaultdict(int)
cnt_y = defaultdict(int)

for _ in range(3):
    a, b = sys.stdin.readline().rstrip().split()
    cnt_x[a] += 1
    cnt_y[b] += 1

answer = []

for key, value in cnt_x.items():
    if value == 1:
        answer.append(key)

for key, value in cnt_y.items():
    if value == 1:
        answer.append(key)

print(*answer)
