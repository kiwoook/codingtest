import sys
from collections import defaultdict

graph = defaultdict(list)
n = int(sys.stdin.readline().rstrip())

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    t, k = map(int, sys.stdin.readline().rstrip().split())
    if t == 1:
        # 단절점에 대한 질의
        if len(graph[k]) >= 2:
            print("yes")
        else:
            print("no")
    if t == 2:
        print("yes")
