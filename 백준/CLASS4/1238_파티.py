import heapq
import sys
from collections import defaultdict

INF = int(1e9)


def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[start][i[0]]:
                distance[start][i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


n, m, x = map(int, sys.stdin.readline().rstrip().split())

distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
graph = defaultdict(list)
for _ in range(m):
    start, end, value = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((end, value))

max_value = 0
for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    max_value = max(max_value, distance[i][x] + distance[x][i])

print(max_value)