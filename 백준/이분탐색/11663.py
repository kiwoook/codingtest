import sys
from bisect import bisect_right, bisect_left, bisect

n, m = map(int, sys.stdin.readline().rstrip().split())

dot_list = list(map(int, sys.stdin.readline().rstrip().split()))
dot_list.sort()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    left_idx = bisect_left(dot_list, a)
    right_idx = bisect_right(dot_list, b)

    print(right_idx - left_idx)