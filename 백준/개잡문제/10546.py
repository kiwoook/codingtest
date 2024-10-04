import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
cnt_dict = defaultdict(int)

for _ in range(n):
    v = sys.stdin.readline().rstrip()
    cnt_dict[v] += 1

for _ in range(n - 1):
    v = sys.stdin.readline().rstrip()
    cnt_dict[v] -= 1
    if cnt_dict[v] == 0:
        del cnt_dict[v]
