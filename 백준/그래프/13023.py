import sys
from collections import defaultdict

sw = 0


def dfs(pos, depth, visited):
    global sw

    if sw == 1:
        return

    if depth == 4:
        sw = 1
        return

    for node in graph[pos]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, depth + 1, visited)
            visited[node] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(n):
    visited = [0 for _ in range(n)]
    visited[idx] = 1
    dfs(idx, 0, visited)
    visited[idx] = 0

print(sw)
