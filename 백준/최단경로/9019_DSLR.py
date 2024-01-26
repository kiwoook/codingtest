import sys
from collections import deque

T = int(input())

for _ in range(T):
    value, result = sys.stdin.readline().rstrip().split()
    value_list = deque([int(v) for v in value])

    q = deque([])
