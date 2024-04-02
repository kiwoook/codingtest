import sys
from collections import defaultdict


def dfs(pos, target_end, weight):
    global answer
    visited[pos] = 1

    if pos == target_end:
        answer = weight
        return

    for node, value in graph[pos]:
        if visited[node] == 0:
            dfs(node, target_end, weight + value)
    visited[pos] = 0


graph = defaultdict(list)

n, m = map(int, sys.stdin.readline().rstrip().split())


for _ in range(n-1):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

for _ in range(m):
    visited = [0 for _ in range(n + 1)]
    start, end = map(int, sys.stdin.readline().rstrip().split())
    answer = 0
    dfs(start, end, 0)
    print(answer)
