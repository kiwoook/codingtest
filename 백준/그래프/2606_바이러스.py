from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

while q:
    v = q.popleft()
    if visited[v] == 0:
        visited[v] = 1
        for m in graph[v]:
            q.append(m)

print(sum(visited) - 1)
