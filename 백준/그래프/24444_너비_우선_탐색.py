from collections import deque


def bfs(graph, v, visited):
    global cnt

    q = deque([v])

    while q:
        k = q.popleft()
        if visited[k] == 0:
            visited[k] = cnt
            cnt += 1
            for z in graph[k]:
                q.append(z)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

cnt = 1
bfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
