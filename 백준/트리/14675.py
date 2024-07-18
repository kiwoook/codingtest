import sys
from collections import defaultdict

def dot(node):
    visited = [0 for _ in range()]

graph = defaultdict(list)
n = int(sys.stdin.readline().rstrip())
history_path = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    history_path.append((a, b))

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    t, k = map(int, sys.stdin.readline().rstrip().split())
