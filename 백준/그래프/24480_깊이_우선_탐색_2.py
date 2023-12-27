import sys

sys.setrecursionlimit(200000)


def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt

    for k in graph[v]:
        if visited[k] == 0:
            cnt += 1
            dfs(graph, k, visited)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

cnt = 1
dfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
