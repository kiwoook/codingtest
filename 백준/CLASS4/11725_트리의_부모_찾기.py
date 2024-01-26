import sys
from collections import defaultdict

sys.setrecursionlimit(10001)

def dfs(node):
    global visited, distance

    visited[node] = 1

    for neighbor, weight in graph[node]:
        if visited[neighbor] == 0:
            distance[neighbor] = distance[node] + weight
            dfs(neighbor)


n = int(input())

graph = defaultdict(list)
tree = defaultdict(list)

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    tree[a].append((b, c))

distance = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

dfs(1)

max_node = 0
max_distance = 0
for idx, x in enumerate(distance):
    if x >= max_distance:
        max_distance = x
        max_node = idx

visited = [0 for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]
dfs(max_node)
print(max(distance))
