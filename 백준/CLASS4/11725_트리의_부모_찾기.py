import sys
from collections import defaultdict, deque


def bfs(start):
    visited = [False] * (n + 1)
    parent_dict = {}

    q = deque([start])

    while q:
        node = q.popleft()
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                parent_dict[neighbor] = node

    return parent_dict


n = int(input())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

parent_dict = bfs(1)

for i in range(2, n + 1):
    print(parent_dict[i])
