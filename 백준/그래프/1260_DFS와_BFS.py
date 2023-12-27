from collections import deque


def dfs(graph, v, visited):
    global move_list

    visited[v] = 1
    move_list.append(str(v))

    for k in graph[v]:
        if visited[k] == 0:
            dfs(graph, k, visited)


def bfs(graph, v):
    move_list2 = []
    bfs_visited = [0 for _ in range(n + 1)]
    q = deque([v])

    while q:
        k = q.popleft()

        if bfs_visited[k] == 0:
            move_list2.append(str(k))
            bfs_visited[k] = 1
            for z in graph[k]:
                q.append(z)

    return ' '.join(move_list2)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [0 for _ in range(n + 1)]

move_list = []
dfs(graph, r, visited)
print(' '.join(move_list))

visited = [0 for _ in range(n + 1)]
print(bfs(graph, r))
