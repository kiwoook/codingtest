import sys
from collections import defaultdict

sys.setrecursionlimit(100001)


def dfs(node):
    global visited, distance

    visited[node] = True

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distance[neighbor] = distance[node] + weight
            dfs(neighbor)


v = int(input())
graph = defaultdict(list)

for _ in range(v):
    cmd_list = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range((len(cmd_list) - 2) // 2):
        graph[cmd_list[0]].append((cmd_list[i * 2 + 1], cmd_list[i * 2 + 2]))

distance = [0 for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
dfs(1)

max_distance = max(distance)
max_idx = 0
for node_idx, weight in enumerate(distance):
    if weight == max_distance:
        max_idx = node_idx

distance = [0 for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]
dfs(max_idx)

print(max(distance))
