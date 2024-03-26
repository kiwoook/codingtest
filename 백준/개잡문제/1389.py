import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for middle in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][end] > graph[start][middle] + graph[middle][end]:
                graph[start][end] = graph[start][middle] + graph[middle][end]

min_sum = INF
answer = 0
for i in range(n, 0, -1):
    tmp_sum = 0
    for k in range(1, n + 1):
        if i != k:
            tmp_sum += graph[i][k]
    if min_sum >= tmp_sum:
        answer = i
        min_sum = tmp_sum
print(answer)
