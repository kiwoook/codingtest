import sys


def return_path(u, v):
    if next_node[u][v] == -1:
        return []

    path = [u]
    while u != v:
        u = next_node[u][v]
        if u == -1:
            return []
        path.append(u)
    return path


INF = int(1e12)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
next_node = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    graph[i][i] = 0
    for j in range(1, n + 1):
        if graph[i][j] < INF:
            next_node[i][j] = j

# 플로이드-워셜 알고리즘 수행
for middle in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][end] > graph[start][middle] + graph[middle][end]:
                graph[start][end] = graph[start][middle] + graph[middle][end]
                next_node[start][end] = next_node[start][middle]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for start in range(1, n + 1):
    for end in range(1, n + 1):
        path = return_path(start, end)
        if len(path) == 1:
            print(0)
        else:
            print(len(path), *path)