import sys
from collections import defaultdict

INF = int(1e9)

v, e = map(int, input().split())
graph = defaultdict(list)
distance = [[INF for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    a, b, c, = map(int, sys.stdin.readline().strip().split())
    distance[a][b] = c
    graph[a].append(b)

for k in range(v + 1):
    for a in range(v + 1):
        for b in range(v + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

answer = INF

for i in range(1, v + 1):
    answer = min(answer, distance[i][i])

if answer == INF:
    print("-1")
else:
    print(answer)
